"""Pure/mocked regression tests: no PDF/ZIP/TeX artifact is produced."""
import hashlib
import copy
import importlib.util
import json
import os
from pathlib import Path
import stat
import sys
import tempfile
import types
import unittest
from unittest.mock import patch
sys.dont_write_bytecode = True
import cumulative_source as source
from cumulative_reader import chapter_ranges, namespace, remote_stem, internal_remote_target, rewrite_link_action

def mock_master():
    value=json.loads(Path(__file__).with_name('cumulative-master.json').read_bytes())
    value['chapters']=[{'stem':'sets','title':'Sets'}]
    return value

class MockObjects:
    def __init__(self, current=None, baseline=None):
        support = {('tools/'+name):b'helper' for name in source.REQUIRED_TOOLS}
        support['tools/cumulative-master.json'] = source.canonical_json(mock_master())
        base = {'sets.tex':b'\\input{preamble}\n\\bibliography{my}\n',
                'preamble.tex':b'\\documentclass{stacks-project}\n\\usepackage{amsmath}\n',
                'stacks-project.cls':b'local class', 'my.bib':b'bibliography', 'COPYING':b'license'}
        self.values={'c':{**base,**support,**(current or {})},'b':{**base,**(baseline or {})}}
    def tree(self, commit):
        return {p:{'mode':'100644','kind':'blob','blob':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()}
                for p,raw in self.values[commit[0]].items()}
    def blob(self,commit,path):
        return self.values[commit[0]][path]

def fixture_inventory(obj=None):
    obj=obj or MockObjects(current={'sets.tex':b'\\input{preamble}\n\\label{section-example}\n'})
    return obj,source.make_inventory(obj,'c'*40,'b'*40,['sets'])

def write_native_fixture(root,obj,inventory):
    root.mkdir()
    for row in inventory['members']:
        path=root/row['archive_path']
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_bytes(obj.blob(row['git_commit'],row['git_path']))
    (root/source.METADATA).write_bytes(source.canonical_json(inventory))

def reconstruction_module():
    fake=types.ModuleType('build_fixed_point')
    for name in ('WindowsNamedMutex','TEX_MUTEX_NAME','TEX_MUTEX_TIMEOUT_MS','run','build_state_vector','scan_tex_diagnostics'):
        setattr(fake,name,lambda *a,**k: (_ for _ in ()).throw(AssertionError('no build runner in fixture')))
    with patch.dict(sys.modules,{'build_fixed_point':fake}):
        spec=importlib.util.spec_from_file_location('reconstruction_under_test',Path(__file__).with_name('reconstruct_cumulative.py'))
        module=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    return module

class FakeSourceZip:
    """Real ZipInfo metadata, no ZIP serialization or extraction."""
    comment=b''
    def __init__(self,obj,inventory):
        self.inventory=source.canonical_json(inventory)
        self.data={row['archive_path']:obj.blob(row['git_commit'],row['git_path']) for row in inventory['members']}
        self.data[source.METADATA]=self.inventory
        self.infos=[]
        for name in sorted(self.data):
            info=source.zipfile.ZipInfo(name,(1980,1,1,0,0,0))
            info.create_system=3
            info.external_attr=0o100644<<16
            info.compress_type=source.zipfile.ZIP_DEFLATED
            self.infos.append(info)
    def __enter__(self): return self
    def __exit__(self,*args): return False
    def infolist(self): return self.infos
    def read(self,name): return self.data[name]

class PackagingTests(unittest.TestCase):
    def test_exact_git_members_and_baseline_separation(self):
        table=source.expected_source_members(MockObjects(), 'c','b',['sets'])
        self.assertIn('current/sets.tex',table)
        self.assertIn('baseline/sets.tex',table)
        self.assertEqual(set(table['current/sets.tex']),{'archive_path','git_commit','git_path','git_blob','bytes','sha256'})
        self.assertEqual(table['current/sets.tex']['git_commit'],'c')
        self.assertEqual(table['baseline/sets.tex']['git_commit'],'b')
    def test_full_native_not_changes_only(self):
        table=source.expected_source_members(MockObjects(current={'unused-other.tex':b'preserved','nested/a.sty':b'macros'}),'c','b',['sets'])
        self.assertIn('current/unused-other.tex',table)
        self.assertIn('current/nested/a.sty',table)
    def test_missing_master_fails(self):
        obj=MockObjects(); del obj.values['c']['tools/cumulative-master.json']
        with self.assertRaises(ValueError): source.expected_source_members(obj,'c','b',['sets'])
    def test_missing_include_fails(self):
        obj=MockObjects(current={'sets.tex':b'\\input{missing}'})
        with self.assertRaisesRegex(ValueError,'unresolved native'): source.expected_source_members(obj,'c','b',['sets'])
    def test_dynamic_include_fails(self):
        obj=MockObjects(current={'sets.tex':b'\\input{\\unknown}'})
        with self.assertRaisesRegex(ValueError,'dynamic native'): source.expected_source_members(obj,'c','b',['sets'])
    def test_required_pdf_figure_is_included(self):
        obj=MockObjects(current={'sets.tex':b'\\includegraphics{figures/commuting}', 'figures/commuting.pdf':b'not a real PDF, native mock'})
        self.assertIn('current/figures/commuting.pdf',source.expected_source_members(obj,'c','b',['sets']))
    def test_evidence_pdf_is_not_native_source(self):
        obj=MockObjects(current={'evidence/proof.pdf':b'not included','validation/composition-current.json':b'{}'})
        table=source.expected_source_members(obj,'c','b',['sets'])
        self.assertNotIn('current/evidence/proof.pdf',table)
        self.assertNotIn('current/validation/composition-current.json',table)
    def test_symlink_input_rejected(self):
        obj=MockObjects(); tree=obj.tree
        def changed(commit):
            value=tree(commit); value['sets.tex']['mode']='120000'; return value
        obj.tree=changed
        with self.assertRaisesRegex(ValueError,'regular'): source.expected_source_members(obj,'c','b',['sets'])
    def test_case_collision_rejected(self):
        obj=MockObjects(current={'SETS.tex':b'collision'})
        with self.assertRaisesRegex(ValueError,'case-colliding'): source.expected_source_members(obj,'c','b',['sets'])
    def test_safe_paths(self):
        for path in ('../a','a/../b','/absolute','C:/x','a\\b','a//b'):
            with self.assertRaises(ValueError): source.safe_path(path)
    def test_comments_do_not_create_dependencies(self):
        obj=MockObjects(current={'sets.tex':b'% \\input{missing}\n\\input{preamble}'})
        source.expected_source_members(obj,'c','b',['sets'])
    def test_system_packages_explicit_not_missing_native(self):
        obj=MockObjects(); paths,system=source.native_closure(obj,'c',obj.tree('c'),['sets'])
        self.assertIn('usepackage:amsmath',system)
        self.assertIn('stacks-project.cls',paths)
    def test_class_command_mentions_are_not_input_calls(self):
        obj=MockObjects(current={'stacks-project.cls':b'\\ClassWarning{x}{\\protect\\includegraphics\\MessageBreak}\n\\def\\bibliographystyle#1{ok}'})
        source.expected_source_members(obj,'c','b',['sets'])
    def test_page_ranges_and_total(self):
        rows=chapter_ranges([{'stem':'a','title':'A'},{'stem':'b','title':'B'}],
              [{'stem':'b','pages':3,'bytes':12,'sha256':'B'}, {'stem':'a','pages':2,'bytes':10,'sha256':'A'}])
        self.assertEqual([(r['start_page'],r['end_page']) for r in rows],[(1,2),(3,5)])
    def test_master_build_mismatch_rejected(self):
        with self.assertRaises(ValueError): chapter_ranges([{'stem':'a'}],[])
    def test_namespace_collisions_prevented(self):
        self.assertNotEqual(namespace('sets','Doc-Start'),namespace('algebra','Doc-Start'))
    def test_local_remote_filename(self):
        self.assertEqual(remote_stem('algebra.pdf'),'algebra')
        self.assertEqual(remote_stem({'/F':'derived.pdf'}),'derived')
        for path in ('https://example.test/algebra.pdf','../algebra.pdf','C:\\algebra.pdf'):
            self.assertIsNone(remote_stem(path))
    def test_primary_order(self):
        fake=types.ModuleType('package_direct_successor_pdfs')
        with patch.dict(sys.modules,{'package_direct_successor_pdfs':fake}):
            import importlib
            wrapper=importlib.import_module('package_cumulative_successor')
            reader={'name':'01-cumulative-reader.pdf','role':'cumulative_reader'}
            src={'name':'02-full-cumulative-editable-source.zip','role':'full_cumulative_editable_source'}
            self.assertEqual(wrapper.ordered_assets(reader,src,[{'name':'extra.pdf'}])[:2],[reader,src])
            with self.assertRaises(ValueError): wrapper.ordered_assets(src,reader,[])
    def test_source_zip_reopen_exact_inventory_without_creating_zip(self):
        obj,inventory=fixture_inventory()
        expected=source.validate_inventory_shape(inventory)
        archive=FakeSourceZip(obj,inventory)
        with patch.object(source.zipfile,'ZipFile',return_value=archive):
            source.verify_source_zip('not-created.zip',archive.inventory,expected)
        extra=FakeSourceZip(obj,inventory)
        extra.infos.append(source.zipfile.ZipInfo('unexpected.tex'))
        with patch.object(source.zipfile,'ZipFile',return_value=extra):
            with self.assertRaisesRegex(ValueError,'missing/extra/duplicate'):
                source.verify_source_zip('not-created.zip',extra.inventory,expected)
        corrupt=FakeSourceZip(obj,inventory)
        corrupt.data['current/sets.tex']=b'corrupt'
        with patch.object(source.zipfile,'ZipFile',return_value=corrupt):
            with self.assertRaisesRegex(ValueError,'byte mismatch'):
                source.verify_source_zip('not-created.zip',corrupt.inventory,expected)
    def test_committed_master_matches_exact36_profile(self):
        master=json.loads(Path(__file__).with_name('cumulative-master.json').read_bytes())
        self.assertEqual(len(master['chapters']),36)
        self.assertEqual(len({x['stem'] for x in master['chapters']}),36)
        self.assertEqual(master['chapters'][-1]['stem'],'spaces-perfect')

class ReviewedDefectRegressions(unittest.TestCase):
    def test_01_actual_preparation_never_calls_git(self):
        module=reconstruction_module()
        obj,inventory=fixture_inventory()
        with tempfile.TemporaryDirectory(prefix='native-fixture-',dir=Path(__file__).parent) as temp:
            root=Path(temp)/'extracted'; output=Path(temp)/'rebuilt'
            write_native_fixture(root,obj,inventory)
            with patch.object(source.subprocess,'check_output',side_effect=AssertionError('Git forbidden')), \
                 patch.object(source.subprocess,'run',side_effect=AssertionError('subprocess forbidden')), \
                 patch.object(source.subprocess,'Popen',side_effect=AssertionError('subprocess forbidden')):
                actual,verified,master,labels=module.prepare_reconstruction(root,output)
            self.assertEqual(labels['sets-section-example'],'sets')
            self.assertEqual(labels['index-section-phantom'],'shared-index')
            self.assertEqual(actual,output)
            self.assertFalse((output/'.git').exists())
    def test_01_duplicate_shared_index_provider_is_rejected(self):
        module=reconstruction_module()
        obj,inventory=fixture_inventory(MockObjects(current={'index.tex':b'\\label{section-phantom}'}))
        with tempfile.TemporaryDirectory(prefix='native-fixture-',dir=Path(__file__).parent) as temp:
            root=Path(temp)/'extracted'; write_native_fixture(root,obj,inventory)
            with self.assertRaisesRegex(ValueError,'ambiguous external-reference'):
                module.prepare_reconstruction(root,Path(temp)/'rebuilt')
    def test_02_unlisted_files_and_symlink_are_never_copied(self):
        module=reconstruction_module(); obj,inventory=fixture_inventory()
        with tempfile.TemporaryDirectory(prefix='native-fixture-',dir=Path(__file__).parent) as temp:
            root=Path(temp)/'extracted'; output=Path(temp)/'rebuilt'
            write_native_fixture(root,obj,inventory)
            (root/'current/amsmath.sty').write_bytes(b'unchecked shadow package')
            (root/'current/tools/unlisted.py').write_bytes(b'unchecked program')
            unlisted=root/'current/unlisted-link'
            outside=Path(temp)/'outside'; outside.mkdir(); (outside/'do-not-copy').write_bytes(b'outside')
            try: os.symlink(outside,unlisted,target_is_directory=True)
            except OSError: pass
            original=source.verified_member_bytes
            touched=[]
            def check(root_arg,row,**kwargs):
                touched.append(row['archive_path'])
                return original(root_arg,row,**kwargs)
            with patch.object(module,'verified_member_bytes',side_effect=check):
                module.prepare_reconstruction(root,output)
            self.assertFalse((output/'amsmath.sty').exists())
            self.assertFalse((output/'tools/unlisted.py').exists())
            self.assertFalse((output/'unlisted-link').exists())
            self.assertTrue(set(touched) <= {r['archive_path'] for r in inventory['members']})
    def test_02_changed_member_between_verification_and_copy_fails(self):
        module=reconstruction_module(); obj,inventory=fixture_inventory()
        with tempfile.TemporaryDirectory(prefix='native-fixture-',dir=Path(__file__).parent) as temp:
            root=Path(temp)/'extracted'; output=Path(temp)/'rebuilt'; write_native_fixture(root,obj,inventory)
            verified=source.verify_extracted(root)
            (root/'current/sets.tex').write_bytes(b'changed after verification')
            with self.assertRaisesRegex(ValueError,'byte identity changed'):
                module.copy_verified_current(root,output,verified)
            self.assertFalse((output/'sets.tex').exists())
    def test_03_overlapping_paths_rejected_before_any_mkdir(self):
        module=reconstruction_module(); obj,inventory=fixture_inventory()
        with tempfile.TemporaryDirectory(prefix='native-fixture-',dir=Path(__file__).parent) as temp:
            root=Path(temp)/'extracted'; write_native_fixture(root,obj,inventory)
            invalid=[root,root/'current/tools/new-output',root/'baseline/new-output',root.parent]
            for output in invalid:
                with self.subTest(output=str(output)),patch.object(Path,'mkdir',side_effect=AssertionError('write attempted')):
                    with self.assertRaisesRegex(ValueError,'disjoint'):
                        module.copy_verified_current(root,output,inventory)
            self.assertEqual(module.disjoint_reconstruction_paths(root,Path(temp)/'sibling')[1],Path(temp)/'sibling')
    def test_03_destination_reparse_ancestor_rejected(self):
        module=reconstruction_module()
        with tempfile.TemporaryDirectory(prefix='native-fixture-',dir=Path(__file__).parent) as temp:
            root=Path(temp)/'source'; root.mkdir(); parent=Path(temp)/'destination-parent'; parent.mkdir()
            original=source.os.lstat
            def lstat(path,*args,**kwargs):
                row=original(path,*args,**kwargs)
                if Path(path)==parent:
                    return types.SimpleNamespace(st_mode=row.st_mode,st_file_attributes=1024)
                return row
            with patch.object(source.os,'lstat',side_effect=lstat):
                with self.assertRaisesRegex(ValueError,'reparse'):
                    module.disjoint_reconstruction_paths(root,parent/'out')
    def test_04_transitive_nonstandard_inputs_are_all_retained(self):
        obj=MockObjects(current={'sets.tex':b'\\input{helper.def}',
             'helper.def':b'\\input{needed.inc}', 'needed.inc':b'\\input{nested.body}',
             'nested.body':b'\\input extensionless', 'extensionless':b'final native body'})
        table=source.expected_source_members(obj,'c','b',['sets'])
        for name in ('helper.def','needed.inc','nested.body','extensionless'):
            self.assertIn('current/'+name,table)
    def test_04_bare_dynamic_input_fails_closed(self):
        obj=MockObjects(current={'sets.tex':b'\\def\\bodyfile{needed.inc}\\input\\bodyfile','needed.inc':b'needed'})
        with self.assertRaisesRegex(ValueError,'unsupported/dynamic'):
            source.expected_source_members(obj,'c','b',['sets'])
    def test_04_numeric_bare_input_without_separator_is_retained(self):
        obj=MockObjects(current={'sets.tex':b'\\input2.inc',
                                '2.inc':b'\\input3.body','3.body':b'needed native body'})
        table=source.expected_source_members(obj,'c','b',['sets'])
        self.assertIn('current/2.inc',table)
        self.assertIn('current/3.body',table)
    def test_04_unmatched_supported_dependency_syntax_fails(self):
        for text in (b'\\include\\name',b'\\includegraphics\\figure',b'\\input#1',b'\\input{bad^^name}'):
            with self.subTest(text=text),self.assertRaisesRegex(ValueError,'dynamic'):
                source.expected_source_members(MockObjects(current={'sets.tex':text}),'c','b',['sets'])
    def test_05_malformed_inventory_variants_fail_before_copy(self):
        _,good=fixture_inventory()
        variants=[]
        value=copy.deepcopy(good); value['members']=[]; variants.append(value)
        value=copy.deepcopy(good); value['members'].append(copy.deepcopy(value['members'][0])); variants.append(value)
        value=copy.deepcopy(good); value['master_path']='../outside.json'; variants.append(value)
        value=copy.deepcopy(good); value['members']=[r for r in value['members'] if r['archive_path']!=source.MASTER]; variants.append(value)
        value=copy.deepcopy(good); value['members'][0]['git_commit']='c'*40; variants.append(value)
        value=copy.deepcopy(good); value['members'][0]['git_path']='different.tex'; variants.append(value)
        value=copy.deepcopy(good); value['chapter_stems']=['../sets']; variants.append(value)
        value=copy.deepcopy(good); value['members'][0]['bytes']=True; variants.append(value)
        value=copy.deepcopy(good); value['members'][0]['sha256']='not-a-hash'; variants.append(value)
        value=copy.deepcopy(good); value['members'][0]['git_blob']='x'*40; variants.append(value)
        for value in variants:
            with self.subTest(value=value),patch.object(Path,'mkdir',side_effect=AssertionError('copy/write attempted')):
                with self.assertRaises(ValueError): source.validate_inventory_shape(value)
    def test_05_master_strict_profile_and_json(self):
        master=mock_master(); master['chapters'][0]['stem']='../sets'
        with self.assertRaises(ValueError): source.validate_master(master,['sets'])
        master=mock_master(); master['assembly_script']='../outside.py'
        with self.assertRaises(ValueError): source.validate_master(master,['sets'])
        with self.assertRaisesRegex(ValueError,'duplicate JSON'): source.parse_json(b'{"schema":1,"schema":2}')
    def test_05_metadata_and_member_reparse_points_rejected(self):
        obj,inventory=fixture_inventory()
        with tempfile.TemporaryDirectory(prefix='native-fixture-',dir=Path(__file__).parent) as temp:
            root=Path(temp)/'extracted'; write_native_fixture(root,obj,inventory)
            original=source.os.lstat
            for bad in (root/source.METADATA,root/'current/tools'):
                def lstat(path,*args,**kwargs):
                    row=original(path,*args,**kwargs)
                    if Path(path)==bad: return types.SimpleNamespace(st_mode=row.st_mode,st_file_attributes=1024)
                    return row
                with self.subTest(bad=str(bad)),patch.object(source.os,'lstat',side_effect=lstat):
                    with self.assertRaisesRegex(ValueError,'reparse'): source.verify_extracted(root)
    def test_06_windows_unsafe_aliases_fail(self):
        examples=['CON.tex','aux.txt','a./b.tex','a /b.tex','a<b.tex','nul\x00.tex',
                  'CLOCK$.txt','conin$.tex','COM1.py','Lpt9.txt','COM\u00b9.tex','a?.tex','a|b','CON .tex']
        for name in examples:
            with self.subTest(name=name),self.assertRaises(ValueError): source.safe_path(name)
    def test_06_zip_symlink_directory_encryption_platform_fail(self):
        obj,inventory=fixture_inventory(); expected=source.validate_inventory_shape(inventory)
        for mode,platform,flags in [(0o120777,3,0),(0o040755,3,0),(0o100644,3,1),(0o100644,0,0)]:
            archive=FakeSourceZip(obj,inventory)
            archive.infos[0].external_attr=mode<<16
            archive.infos[0].create_system=platform
            archive.infos[0].flag_bits=flags
            with self.subTest(mode=mode,platform=platform,flags=flags),patch.object(source.zipfile,'ZipFile',return_value=archive):
                with self.assertRaisesRegex(ValueError,'regular file'):
                    source.verify_source_zip('not-created.zip',archive.inventory,expected)
    def test_07_other_directory_action_retains_exact_target(self):
        self.assertIsNone(remote_stem('other-edition/algebra.pdf'))
        original={'/S':'/GoToR','/F':'other-edition/algebra.pdf','/D':'section.3'}
        result,disposition=rewrite_link_action(original,'sets',{'sets','algebra'},
                  lambda *a,**k: (_ for _ in ()).throw(AssertionError('must not internalize')),copy.deepcopy)
        self.assertEqual(disposition,'external')
        self.assertEqual(result,original)
        self.assertEqual(internal_remote_target({'/S':'/GoToR','/F':'algebra.pdf'},{'algebra'}),'algebra')

if __name__ == '__main__': unittest.main()
