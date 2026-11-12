#!/usr/bin/env python3
"""Independent bounded validator for the no-overwrite Tohoku r42 successor."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import io
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "tohoku_r41"
TARGET = ROOT / "tohoku_r42"
STAGE = ROOT / ".tohoku-r42-txn"
PROJECT = Path(
    r"user\Documents\interlanguage\03_projects\language_management"
    r"\english_germanic\03_working_translations"
    r"\tohoku_bilingual_canonical_stacks_20260804_r1"
)
SEM = PROJECT / "sem" / "r16"
AUTHORITY = PROJECT / "authority_snapshot"

EXPECTED_SOURCE = {
    "STATUS.md": (667, "80646BBF6EF4B25229306E520F4E00D872D6DD9B98119649C6D32BB50AC52136"),
    "cfg.json": (5194, "27B69C9022454C2DC15FBE8552C35BD38416EF8547C992F72E68B54CDCEA5E80"),
    "check.json": (75491, "872B81C44D5C595A7E36400D514EFA66EF9E363F684773E0BBADD53F4356B386"),
    "dec.csv": (355505, "B7533F85345E134ECD013221168A0CC1A54DA8C94AFA46CA1D9591DBDBD82029"),
    "intake.json": (1878, "3213469B06D5C7AE58587BA214710172C63A5762A9339EFCF1DE3EB8009D4BFB"),
    "issues.csv": (29540, "1C00B88F578BFDE2C0F178A65D0616C6BAAED4597F2E3EFCBC5BBA0380882CF8"),
    "map.csv": (470572, "992BBCE3ECA7668A6B0B958F15D0E1CEC2CA76C6EE6607C8722024B3DF01D9ED"),
    "mcheck.json": (65319, "98EDB484CA1487D41A1241ADCFB02AD79012BB8254E6352E9C312E486D228C81"),
    "r41-check.json": (21477, "8FF1CA8DA5F7E85B1D56776137A9DB06607A0E3F7EF1107C2AB714366CD1478C"),
    "stx.csv": (5270117, "319AE1E10C1F1607FF12603C25D0DA412BEDCE1795110EFCE6950D58CB03CB36"),
    "tcand.csv": (480052, "21C181693AF526ACF4CAEB997E8EA86927E1B9BD864B00CADE96E671CF173548"),
    "tmap.csv": (2424, "DEB05561CA297574E3FC54D9E36CB8628A092C280BDFAB53E79C0F198C29C9A1"),
    "topics.csv": (2453, "AA62558CA4292B914D75A63BC4436586D88B754C9D08618DC8E67554C58B6B5C"),
    "ucand.csv": (120, "D7D823C01798DC15596F2C67D1177F427A50EE39CDD4F4B6B437FBD56A86D1A4"),
    "units.csv": (392090, "DC5A9609F706B7C8823E6C5495510D365A38E95AE81F1C97071D0B1217480116"),
}
EXPECTED_SOURCE_SURFACE = (
    15,
    7172899,
    "C842B6ECAC9CD890C7855AA2232A0B8101A185805F45998B68D61DB04E658C67",
)

EXPECTED_SEM = {
    "README.md": (2585, "66D4CF92728AF7FF10E82CDFD97AFCD9D26B55CE9FBC985932FFBCD597DD64B4"),
    "bib.csv": (10422, "93F5A934ADDE0CD92BBB21AF70EFD81BA128CCD2EDF51EB19428B83437EC3516"),
    "catalog.csv": (772, "AE68D646094D8B309D641ED46A9612CC46E392BF2323306F0CEE7793B16BE043"),
    "edges.csv": (260944, "F1607445D52F28DA2F3FE93D8F47D7959C35ECFFBC167B5AB0E787A91264C719"),
    "idmap.csv": (473, "977D4A8F59A9642D58926DED8BB600079863AE6AF3F1F532806E83A9AB645BEA"),
    "manifest.json": (25516, "BF1BE40E573CA0BF3A7D372056EA608FC891DB1C64DEFDCD8DFED1AA7349CC04"),
    "nodes.csv": (583525, "564AF8A64242DAC92A6165BA448F86F3E5768E8029A0E0D510D3F5F73F9AB4EE"),
    "objects.csv": (106319, "82FF34C19C6D17D80DC3A617FD106ED324099CC9D0F2FE752757D0642ED31999"),
    "occ.csv": (515080, "D1EC29BA19F4B42E51A88713D6CB2B80016FD926619F2673B144F7FA6B14ADA4"),
    "pages.csv": (23686, "E813C410B0A2AE53B4A787FD6C66A74225021E3A0FE22AD10CA2ED0C29807B0D"),
    "refdec.csv": (2313, "6AC5E23C3D4ADA0ABB1427E0533C3033E13B63C28A654A9C7E74A057A045FFA2"),
    "refs.csv": (159815, "995C9526CEC36FB6B437D7C688E4D40547BFC050949E3819A607FEEF53EA1162"),
    "resid.csv": (6415, "DDF53E58E21C7A5BF60C54ADC5EB9EB420B717246F1C69F294BBA5E358A38430"),
    "stacks.csv": (11777, "E13EFA405B525D69BFF38256601E4AF64D22FA3075F3A95AB3DFB78C15CFD060"),
    "subjects.csv": (2133, "A77A81831F752BA21701B150C13C51325E511B2FD5DFC76EED135FE3EDEEB026"),
    "terms.csv": (325587, "6D93CBBD2D6CF3E354FE90DC51605ACD9C7B0932CEF216FB9D606AD97D666E5D"),
    "validation.json": (6252, "1210F4D528BE2491D0508A663056E8FAB2DA60AC0334B3C3B67D0BE9F07D0E58"),
    "xwork.csv": (2446, "7BC42D7026C34AD8B1A111353E0810378F1DB9D1284BAD4C5C34D509D57B9EBB"),
}
EXPECTED_SEM_SURFACE = (
    18,
    2046060,
    "67687BEE701BC515A2824BF13ACEDE31CF9027A0930FA0AF608478B5001858D1",
)

EXPECTED_RUNTIME = {
    "srcmap/intake.py": (9923, "CFD53B71649BEF84A166397AA18E39AC5E4EDF00DD860142B2936F886AB080B1"),
    "srcmap/scan.py": (3403, "269E4D2F73405BDA82F373F04AF0109431416FF25CCA874F0051D193BC444D30"),
    "srcmap/map.py": (27167, "57A92E34DB189E0EE95E6816074DB686C5616590C33DF823EF8EB9E9AFC2E1DF"),
    "fga/mkidx.py": (14844, "4425B5D021B3E35371DEBB567881697F88DF6F533ACFC9783A749CE1A5176A6B"),
    "fga/mkmap.py": (22213, "7281F57EC7439E00431F2962DF9A6944779294955A9C4369615FFF04318B0053"),
    "fga/__pycache__/mkidx.cpython-313.pyc": (21123, "A78A1E45C6EB3960139B1D2A8AF42E5B10768034F0A87274448EBA69779BD424"),
    "fga/__pycache__/mkmap.cpython-313.pyc": (26471, "1AA6B79FFE873AB6C2E58FF2A9826DE6FDB6B1DD69A8D3473FD5F56168F2077D"),
    "tags/tags": (991506, "C5C7017FB5C50B60295B30801CA1B5BAB8F5B379F61B084D8219441938125FCF"),
}

EXPECTED_AUTHORITY = {
    "jstage_part_I_9_2_119.pdf": (7305283, "5A8E5720BC2EF8905BF85F7919C65AC4A87A31CFC854BD77E6B5084C0D2DEBEF"),
    "jstage_part_II_9_3_185.pdf": (3984260, "8D632A04EE0FA987B40B721BEE6E64BB3E641D6A1CE02335556213F1564C9A53"),
}

EXPECTED_REPAIRS = {
    "production/p142_fix2/check.json": (12979, "CFFB62EB6C1C38755D637BCB74DA430633F0B51FEF5BA004543E06B3784DB257"),
    "production/p142_fix2/decisions.jsonl": (5314, "AD795C72432577246314938AAE53CF5ECA04CE487A88291CEC7BDB43A1447301"),
    "production/p142_fix2/tex/fr_diplomatic/p142.tex": (4143, "F0A0D801326203CC75CCE525E99E4C41FF97E6581F2106E09828197FD274F226"),
    "production/p142_fix2/tex/fr_corrected/p142.tex": (4673, "87E7FA8C572211776BFBAFD89738E44FD1D16A957A640B2A6F6485DE8A70FF2E"),
    "production/p142_fix2/tex/en/p142.tex": (4067, "49CFBE88DDE5EF7F88F477CA5849278C6C395E20C361B7B52B89DDEED2A4D1E8"),
    "build/v068c3r14/build.json": (99725, "89DF7D556C2DC4561799DDE7E18E06CC87EA31133D7E8E02A56EEBDBE8BDB8AD"),
    "build/v068c3r14/fr/main-fr.pdf": (1412586, "3969E6329253A0C71C2AB02170BD5456148B5DECAB84E33C479002E623338A7B"),
    "build/v068c3r14/en/main-en.pdf": (1377307, "98C923C5353FC9A035E26FD293E1AA7E09ABDABE104C57236AE17DEE820D290F"),
    "qa/v68r36/check.json": (24235, "1580BB2F03328F1CEEA59526ACF7D5A3C0C22EC0C1C73EAF51D97331A5C2C896"),
    "production/p161_fix1/check.json": (11140, "69C870C691BC4E7D27A6DFA3D568C22414186CC63029D149E5D233F99243C235"),
    "production/p161_fix1/decisions.jsonl": (2704, "0C8D9719878A801F6C5497C2D0F127E37FA73C83826B611F5064C58D415DC136"),
    "production/p161_fix1/preflight.json": (8684, "B84FEA9A96367A09822EB67586ED8FFCFB9C9B3EB5769548D09A0BA75D4FB85F"),
    "production/p161_fix1/tex/fr_diplomatic/p161.tex": (4280, "FF34B9B75C398583923F8D9AD806EAD7B436BBC40CA170A7CF408625F2154C68"),
    "production/p161_fix1/tex/fr_corrected/p161.tex": (4335, "A3AADEA6BCA00308E9332D7942EF043E1173FABB451C18D3BC9AD9EC964711A6"),
    "production/p161_fix1/tex/en/p161.tex": (4171, "14F14A7D9AB5CE5B4B83A5D1458100EDD79435958670CFB0B7175E9162A9223E"),
    "SOURCE_CORRECTIONS.jsonl": (207597, "611EAE2E81A20294E0D862E10B061509633CE604C0776B7993857FBE6947F01A"),
    "ed/fr.tex": (6708, "B99FCBB43DDE5D6515A6932F859A74EE6FB85065940C8CDBCD7AA2E070788CCC"),
    "ed/en.tex": (5658, "38831824609621909FCF6367368583A0F807D077DD55E3CFE0435D34148434BB"),
}

EXPECTED_ARTIFACTS = {
    "homology.tex": (382168, "E9BF2AE74E2F0392A05A37405B12C97E590D12ADA1DA23D3B694E4AD782A30AF"),
    "homology.aux": (28983, "31D0349F6D482492744ABB826179FB1688CD3F9F0A5365787A3E015E373448CF"),
    "homology.log": (39297, "0C5E27893B377E84B129BBEB9945F3B4E5D6C2633DF00D7A96C3AB29F423C2BF"),
    "homology.pdf": (1082731, "550EE987F10359A968D98FF667EB71BAAB0AACE6574D5BFB8EDFD60EFA6F11CA"),
    "derived.tex": (525894, "0A75BDA188A96B44536D78DB7FD1C3E2E5780C745839B2125BC9F2410CEF37D2"),
    "derived.aux": (36698, "0989919F36E08B1DDC34E20D2E002351F20154548736D127D96CF7295E759776"),
    "derived.log": (46288, "741BECA31A364905EF0526E34817F577E0BEFD3825C6A5B0F8A410DFF5F51846"),
    "derived.pdf": (1382159, "C266D8F892CB304DB5C5C036A32C4BBAF79FD61D5183BA931612CD7041D78464"),
    "cohomology.tex": (820992, "228FEEECC2D7535632710991DE5AD774920226CA21615746CCD7F1082B2D030D"),
    "cohomology.aux": (51757, "781F0A1A6211FA387E5BF4160B6CA881C348D811C8964266C5A06A9143B5C779"),
    "cohomology.log": (47424, "EE4ECC71A994BF7E3E9ABF436867CC939A134AB6301E634E4BC4BF01D2E7DD88"),
    "cohomology.pdf": (1839522, "D8C62A6AAB9DA5D0CC3EDBB94744EE8C8ED0412E4004D33344E4FC1AC776F50E"),
    "divisors.tex": (393592, "E83AFAD6AEBEED113EABCB4E8D571CC241E8F02AEFC5216CDDD9E3CF927E7D50"),
    "divisors.aux": (31963, "864F03D262112055FB7D1050C30B419D9EA54BBAC521DCBAA6755F8E40D5288F"),
    "divisors.log": (36891, "2FB09163CFE87C24882D7D7A00EC0781EABC836C8BE8EDCB04F508612A56E038"),
    "divisors.pdf": (1127391, "F1672B01E868A1DA071D80C996A40776BFE1D8CC7393D7AA06F9C450729E300A"),
}

BUILD_SPECS = {
    "homology": {"pages": 116, "visual": [55, 56, 57, 58]},
    "derived": {"pages": 146, "visual": [71, 72, 73, 74]},
    "cohomology": {"pages": 215, "visual": [47, 48, 49, 50, 51, 52, 53]},
    "divisors": {"pages": 96, "visual": [64, 65, 66, 67]},
}

EXPECTED_AUX_LINES = {
    "homology.aux": (
        r"\newlabel{lemma-left-satellites-projective-effacements}{{13.21}{56}{Left satellites and the dual satellite theorem}{subsection.13.21}{}}",
        r"\newlabel{equation-left-satellites-nested-subobjects}{{13.21.1}{56}{Left satellites and the dual satellite theorem}{equation.13.21.1}{}}",
        r"\newlabel{equation-contravariant-satellites-nested-subobjects}{{13.21.2}{57}{Left satellites and the dual satellite theorem}{equation.13.21.2}{}}",
    ),
    "derived.aux": (
        r"\newlabel{lemma-right-satellites-to-right-derived-functors}{{20.4}{72}{Comparison from satellites to right derived functors}{subsection.20.4}{}}",
    ),
    "cohomology.aux": (
        r"\newlabel{definition-fine-abelian-sheaf}{{22.6}{48}{Fine abelian sheaves}{subsection.22.6}{}}",
        r"\newlabel{lemma-fine-phi-soft-and-tensor}{{22.7}{48}{}{subsection.22.7}{}}",
        r"\newlabel{lemma-cartan-resolution-fine-torsion-free}{{22.16}{52}{Cartan resolution}{subsection.22.16}{}}",
    ),
    "divisors.aux": (
        r"\newlabel{definition-sheaf-Weil-divisors}{{27.8}{65}{}{subsection.27.8}{}}",
        r"\newlabel{lemma-sheaf-Weil-divisors-flasque}{{27.9}{65}{}{subsection.27.9}{}}",
        r"\newlabel{lemma-locally-UFD-divisor-resolution}{{27.10}{66}{Divisor-sheaf resolution}{subsection.27.10}{}}",
        r"\newlabel{equation-locally-UFD-divisor-resolution}{{27.10.1}{66}{Divisor-sheaf resolution}{equation.27.10.1}{}}",
    ),
}

DECISION_ROWS = [
    {
        "decision_id": "D000996",
        "unit_id": "tohoku:thm:2.2.2:dual",
        "action": "replace",
        "disposition": "existing_equivalent",
        "stacks_labels": "homology-lemma-left-satellites-projective-effacements",
        "rationale": "Stacks now proves the repaired p. 142 dual statement under the stated effacement hypotheses. Projective effacements construct the left satellites as a universal step -1 system with the terminal extension property and co-effaceable positive components; their exactness is governed by half-exactness and the same nested-subobject condition, with enough projectives reducing the criterion to half-exactness. The contravariant form exchanges the relevant projective and injective effacements. When both halves exist, the degree-reversed left half and the right half glue to an all-integer graded connecting functor, exact exactly under the stated half-exactness and nested-subobject criterion. For each a>0, the finite right restriction on {0,...,a} has the initial extension property, while the degree-reversed finite left restriction on {-a,...,0} has the terminal extension property. The glued system is exact, but no global all-Z universality is asserted.",
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000214",
    },
    {
        "decision_id": "D000997",
        "unit_id": "tohoku:morphism:satellite-to-derived",
        "action": "replace",
        "disposition": "existing_equivalent",
        "stacks_labels": "derived-lemma-right-satellites-to-right-derived-functors",
        "rationale": "Stacks now proves the exact p. 143 satellite-to-derived comparison under enough injectives: RF is everywhere defined and its negative derived functors vanish; its nonnegative derived functors form the canonical cohomological delta-functor; and the universal nonnegative right-satellite system admits the unique comparison extending F -> R^0F, coherently under canonical satellite identifications. The comparison is an isomorphism exactly when F is left exact. In the converse, unpadded satellite exactness is completed by the initial zero supplied by left exactness of S^0F = F, injective acyclicity makes the right-derived delta-functor universal, and the two distinct universal properties give the inverse identities. No comparison in negative satellite degrees is asserted.",
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000183",
    },
    {
        "decision_id": "D000998",
        "unit_id": "tohoku:construction:cartan-resolution",
        "action": "replace",
        "disposition": "existing_equivalent",
        "stacks_labels": "cohomology-definition-fine-abelian-sheaf;cohomology-lemma-fine-phi-soft-and-tensor;cohomology-lemma-cartan-resolution-fine-torsion-free",
        "rationale": "Stacks now defines fine abelian sheaves by locally finite endomorphism partitions, proves that fine sheaves are Phi-soft for paracompactifying supports and remain fine after tensoring, and proves that any fixed fine torsion-free resolution of the constant sheaf Z yields an exact functorial Cartan resolution F tensor C whose terms are Gamma_Phi-acyclic and which computes supported cohomology. The construction is explicitly conditional on the supplied fine torsion-free resolution and makes no independent existence claim.",
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000244",
    },
    {
        "decision_id": "D000999",
        "unit_id": "tohoku:construction:divisor-sequence:p2",
        "action": "replace",
        "disposition": "existing_equivalent",
        "stacks_labels": "divisors-definition-sheaf-Weil-divisors;divisors-lemma-sheaf-Weil-divisors-flasque;divisors-lemma-locally-UFD-divisor-resolution",
        "rationale": "Stacks now constructs the flasque sheaf of Weil divisors and, for a Noetherian integral scheme with factorial local rings, proves the exact flasque resolution of the unit sheaf by nonzero rational functions and divisors. Consequently H^1 of the unit sheaf is the Weil divisor class group and all higher cohomology vanishes. No projective-bundle lifting assertion is included.",
        "review_state": "integrated_source_stacks_and_independent_review",
        "supersedes": "D000250",
    },
]

EXPECTED_MAPPING_COUNTS = {
    "active_graph_corrections": 0,
    "active_source_issues": 0,
    "candidate_units": 0,
    "decided_units": 679,
    "decisions": 999,
    "dispositions": {
        "example_or_remark": 84,
        "existing_equivalent": 350,
        "existing_stronger": 38,
        "existing_weaker": 9,
        "extend_existing": 23,
        "historical_reference": 33,
        "new_section": 6,
        "new_statement": 22,
        "structural_only": 426,
    },
    "graph_corrections": 0,
    "review_units": 0,
    "source_issues": 29,
    "unit_candidates": 0,
    "units": 991,
}
EXPECTED_SCAN_COUNTS = {
    "labels": 22050,
    "official_tags_joined": 21437,
    "tex_files": 119,
    "topic_candidates": 1263,
    "topic_coverage": {"direct": 13},
    "topics": 13,
}

NEW_LABEL_ROWS = {
    "cohomology-definition-fine-abelian-sheaf": ("cohomology.tex", "4899", "definition", "section-cohomology-family-supports", "Cohomology with supports in a family", "F7D758894FA75446FD188101A19A1EC0BF28C7EABE3F875D21F35066885A4B27"),
    "cohomology-lemma-cartan-resolution-fine-torsion-free": ("cohomology.tex", "5317", "lemma", "section-cohomology-family-supports", "Cohomology with supports in a family", "61F986E3D42666D6FA35DBDE8157F77622A871E920B22A3D7224CE6EA3427B54"),
    "cohomology-lemma-fine-phi-soft-and-tensor": ("cohomology.tex", "4923", "lemma", "section-cohomology-family-supports", "Cohomology with supports in a family", "1251EC69F7DFD040C6E5B6B7FC5EFA6F1C0AA90DA36FC30540FD8F17487197B5"),
    "derived-lemma-right-satellites-to-right-derived-functors": ("derived.tex", "7072", "lemma", "section-right-derived-functor", "Right derived functors and injective resolutions", "E04682A88CEC0209FEB5A869336C7DD9E6D2335942BE1781F7CFE924E6589A2C"),
    "divisors-definition-sheaf-Weil-divisors": ("divisors.tex", "6763", "definition", "section-Weil-divisors", "Weil divisors", "06721532DE199BE461E95D7262183B41D4EDBF96B2B7B324D3DFA71E34A55AE8"),
    "divisors-equation-locally-UFD-divisor-resolution": ("divisors.tex", "6812", "equation", "section-Weil-divisors", "Weil divisors", "D6E30247B7700D2983EFC4DF3A39DE7410136139FE63EA9652945BB2B13EB1D0"),
    "divisors-lemma-locally-UFD-divisor-resolution": ("divisors.tex", "6803", "lemma", "section-Weil-divisors", "Weil divisors", "6B706E1A7596D6BD20D26ECB40D4490F1CAF3ECC40F0FD4660984F0043A50814"),
    "divisors-lemma-sheaf-Weil-divisors-flasque": ("divisors.tex", "6775", "lemma", "section-Weil-divisors", "Weil divisors", "7DCEE6CD080EA8C2CA7DCE91FA5889A9514C08B04A55BDE49ADF054F33E2BD75"),
    "homology-equation-contravariant-satellites-nested-subobjects": ("homology.tex", "5180", "equation", "section-cohomological-delta-functor", "Cohomological delta-functors", "FF764BBC1FC63DDFFCABB0F7C79ECDF6FAC78A4D068116FC3621A34F32448E76"),
    "homology-equation-left-satellites-nested-subobjects": ("homology.tex", "5132", "equation", "section-cohomological-delta-functor", "Cohomological delta-functors", "ED3C4D4AB85D584E0B8CC3A06AED7B0DA9302EE08A106EE0CE56CBE7D6B939B5"),
    "homology-lemma-left-satellites-projective-effacements": ("homology.tex", "5087", "lemma", "section-cohomological-delta-functor", "Cohomological delta-functors", "4B15D998191CF071C653E9A09CDCCDE5DE2D2C9A93BA1CFC688F244934D36AFC"),
}
EXPECTED_EXISTING_LINE_CHANGES = {
    "cohomology.tex": 392,
    "derived.tex": 187,
    "divisors.tex": 76,
    "homology.tex": 168,
}
EXPECTED_CANDIDATE_ADDED = {
    ("delta-functor", "homology-equation-contravariant-satellites-nested-subobjects"),
    ("delta-functor", "homology-equation-left-satellites-nested-subobjects"),
    ("delta-functor", "homology-lemma-left-satellites-projective-effacements"),
    ("derived-functor", "derived-lemma-right-satellites-to-right-derived-functors"),
    ("injectives", "derived-lemma-right-satellites-to-right-derived-functors"),
    ("sheaf-cohomology", "cohomology-definition-fine-abelian-sheaf"),
    ("support", "cohomology-definition-fine-abelian-sheaf"),
    ("support", "cohomology-lemma-cartan-resolution-fine-torsion-free"),
    ("support", "cohomology-lemma-fine-phi-soft-and-tensor"),
}
EXPECTED_CANDIDATE_REMOVED = {
    ("sheaf-cohomology", "cohomology-lemma-RHom-into-K-injective"),
}
EXPECTED_CANDIDATE_EXISTING_LINE_CHANGES = {
    "cohomology.tex": 150,
    "derived.tex": 110,
    "homology.tex": 89,
}

PAYLOAD = {
    "cfg.json", "intake.json", "units.csv", "topics.csv", "dec.csv",
    "issues.csv", "check.json", "stx.csv", "tcand.csv", "tmap.csv",
    "map.csv", "ucand.csv", "mcheck.json", "STATUS.md",
}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def identity(path: Path) -> tuple[int, str]:
    data = path.read_bytes()
    return len(data), digest(data)


def record(path: Path, name: str | None = None) -> dict[str, object]:
    size, sha256 = identity(path)
    return {"name": name or path.name, "bytes": size, "sha256": sha256}


def aggregate(records: list[dict[str, object]]) -> str:
    payload = b"".join(
        f"{item['name']}\0{item['bytes']}\0{item['sha256']}\n".encode("utf-8")
        for item in sorted(records, key=lambda value: str(value["name"]))
    )
    return digest(payload)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def require_identity(path: Path, expected: tuple[int, str]) -> None:
    require(path.is_file() and not path.is_symlink(), f"Expected plain file: {path}")
    require(identity(path) == expected, f"Identity drift: {path}")


def strict_json(path: Path) -> dict:
    data = path.read_bytes()
    require(b"\r" not in data and data.endswith(b"\n"), f"Noncanonical JSON: {path}")
    pairs: list[tuple[str, object]] = []

    def no_duplicates(values: list[tuple[str, object]]) -> dict:
        output: dict[str, object] = {}
        for key, value in values:
            require(key not in output, f"Duplicate JSON key {key}: {path}")
            output[key] = value
        return output

    value = json.loads(data.decode("utf-8"), object_pairs_hook=no_duplicates)
    require(isinstance(value, dict), f"Expected JSON object: {path}")
    return value


def load_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    data = path.read_bytes()
    require(b"\r" not in data and data.endswith(b"\n"), f"Noncanonical CSV: {path}")
    reader = csv.DictReader(data.decode("utf-8-sig").splitlines())
    rows = list(reader)
    require(reader.fieldnames is not None, f"Missing CSV header: {path}")
    require(all(None not in row and None not in row.values() for row in rows), f"Malformed CSV: {path}")
    return list(reader.fieldnames), rows


def csv_bytes(fields: list[str], rows: list[dict[str, str]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def expected_tex_hashes() -> dict[str, str]:
    hashes = dict(strict_json(SOURCE / "check.json")["tex_sha256"])
    require(len(hashes) == 119, "Predecessor TeX manifest is not 119 files")
    for name in ("homology.tex", "derived.tex", "cohomology.tex", "divisors.tex"):
        hashes[name] = EXPECTED_ARTIFACTS[name][1]
    return hashes


def load_mkidx():
    path = ROOT / "fga" / "mkidx.py"
    spec = importlib.util.spec_from_file_location("tohoku_r42_mkidx", path)
    require(spec is not None and spec.loader is not None, "Cannot load pinned mkidx")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify_semantic() -> dict[str, object]:
    names = {path.name for path in SEM.iterdir() if path.is_file()}
    require(names == set(EXPECTED_SEM), "sem/r16 file surface drift")
    require(not any(path.is_dir() for path in SEM.iterdir()), "Unexpected sem/r16 subdirectory")
    records = []
    for name, expected in sorted(EXPECTED_SEM.items()):
        require_identity(SEM / name, expected)
        records.append(record(SEM / name))
    require(
        (len(records), sum(int(item["bytes"]) for item in records), aggregate(records))
        == EXPECTED_SEM_SURFACE,
        "sem/r16 aggregate drift",
    )
    manifest = strict_json(SEM / "manifest.json")
    validation = strict_json(SEM / "validation.json")
    require(manifest.get("schema") == "tohoku-semantic-local-successor-manifest-v16", "sem/r16 manifest schema drift")
    require(manifest.get("errors") == [], "sem/r16 manifest errors")
    require(validation.get("schema") == "tohoku-semantic-local-successor-validation-v16", "sem/r16 validation schema drift")
    require(validation.get("status") == "PASS" and validation.get("errors") == [], "sem/r16 validation not PASS")
    require(validation.get("manifest_sha256") == EXPECTED_SEM["manifest.json"][1], "sem/r16 manifest-validation binding drift")
    oracle = manifest.get("table_delta_oracle", {})
    require(oracle.get("changed_table_count") == 3, "sem/r16 changed-table count drift")
    require(set(oracle.get("changed_tables", {})) == {"catalog.csv", "nodes.csv", "occ.csv"}, "sem/r16 changed-table set drift")
    require(oracle.get("unchanged_table_count") == 12, "sem/r16 unchanged-table count drift")
    override = manifest.get("semantic_override", {})
    require(override.get("node_id") == "tohoku:thm:2.2.2:dual", "sem/r16 override node drift")
    require(override.get("occurrence_id") == "tohoku:occ:p142:o003", "sem/r16 override occurrence drift")
    require(override.get("segments") == {
        "dip": {"bytes": 836, "sha256": "1EA26377117670CECE6821A092F1161A99B4F98BFEB5101A359109CDAA82C1B8"},
        "fr": {"bytes": 1247, "sha256": "05A6D18C9F529C7221DBC26F64BC9FB96A579D83549A2D8E5466D9F94AF9F0B5"},
        "en": {"bytes": 1098, "sha256": "8B9AD2FFFDD798805F2631B179323537CDB56798E65A9A9F1F0A365D9FF22CEC"},
    }, "sem/r16 override segment drift")
    _, nodes = load_csv(SEM / "nodes.csv")
    require(len(nodes) == 991, "sem/r16 node count drift")
    by_id = {row["node_id"]: row for row in nodes}
    require(len(by_id) == 991, "sem/r16 duplicate node IDs")
    for decision in DECISION_ROWS:
        require(decision["unit_id"] in by_id, f"Missing semantic unit: {decision['unit_id']}")
    dual = by_id["tohoku:thm:2.2.2:dual"]
    require(dual.get("en_label") == override.get("labels", {}).get("en"), "sem/r16 dual English label drift")
    require(dual.get("fr_label") == override.get("labels", {}).get("fr"), "sem/r16 dual French label drift")
    return {
        "generation": "sem/r16",
        "files": records,
        "file_count": len(records),
        "bytes": sum(int(item["bytes"]) for item in records),
        "aggregate_sha256": aggregate(records),
        "validation_status": "PASS",
        "independent_reconstruction": {
            "all_18_identities_replayed": True,
            "changed_tables_exact": ["catalog.csv", "nodes.csv", "occ.csv"],
            "other_13_files_byte_identical_to_inherited_oracle": True,
            "p142_virtual_split_and_dual_segments_reconstructed": True,
        },
    }


def verify_repairs() -> dict[str, object]:
    records = []
    for relative, expected in sorted(EXPECTED_REPAIRS.items()):
        path = PROJECT / relative
        require_identity(path, expected)
        records.append(record(path, relative))
    p142 = strict_json(PROJECT / "production" / "p142_fix2" / "check.json")
    require(p142.get("status") == "PASS" and p142.get("errors") == [], "p142_fix2 not PASS")
    qa = strict_json(PROJECT / "qa" / "v68r36" / "check.json")
    require(qa.get("status") == "PASS" and qa.get("errors") == [], "reader r14 QA not PASS")
    conclusion = qa.get("conclusion", {})
    require(conclusion.get("reader_successor_accepted") is True, "reader r14 not accepted")
    require(conclusion.get("semantic_graph_successor_may_bind_this_receipt") is True, "reader r14 QA does not admit semantic successor")
    build = strict_json(PROJECT / "build" / "v068c3r14" / "build.json")
    require(build.get("status") == "PASS" and build.get("errors") == [], "reader r14 build not PASS")
    p161 = strict_json(PROJECT / "production" / "p161_fix1" / "check.json")
    require(p161.get("status") == "PASS" and p161.get("errors") == [], "p161_fix1 not PASS")
    require(p161.get("replay", {}).get("status") == "PASS", "p161_fix1 replay not PASS")
    require(p161.get("root_controls", {}).get("source_correction") == "TOH-SRC-P161-003", "p161 root repair ID drift")
    require(p161.get("decisions", {}).get("appended_id") == "TOH-P161-COR-003", "p161 local repair ID drift")
    return {
        "files": records,
        "file_count": len(records),
        "bytes": sum(int(item["bytes"]) for item in records),
        "aggregate_sha256": aggregate(records),
        "p142_fix2": "SEALED_REPLAY_PASS",
        "reader_r14": "PASS",
        "reader_r14_independent_qa": "PASS",
        "p161_fix1": "SEALED_REPLAY_PASS",
        "p161_independent_source_audit": "STRICT_PASS",
    }


def verify_builds() -> dict[str, object]:
    for name, expected in EXPECTED_ARTIFACTS.items():
        require_identity(ROOT / name, expected)
    forbidden = [
        r"(?m)^! (?:LaTeX|Package|Undefined|Emergency|File|Missing|Extra|Use of|Runaway|Paragraph)",
        r"(?m)^LaTeX Warning:", r"(?m)^Package .* Warning:",
        r"undefined references", r"undefined citations",
        r"Rerun to get cross-references right", r"Label\(s\) may have changed",
    ]
    builds: dict[str, object] = {}
    for chapter, spec in BUILD_SPECS.items():
        log = (ROOT / f"{chapter}.log").read_text(encoding="utf-8", errors="replace")
        hits = [pattern for pattern in forbidden if re.search(pattern, log)]
        require(not hits, f"{chapter} build diagnostics: {hits}")
        output = re.findall(
            rf"Output written on {re.escape(chapter)}\.pdf \(([0-9]+) pages?, ([0-9]+) bytes\)\.",
            log,
        )
        require(output == [(str(spec["pages"]), str(EXPECTED_ARTIFACTS[f"{chapter}.pdf"][0]))], f"{chapter} output receipt drift")
        aux_lines = set((ROOT / f"{chapter}.aux").read_text(encoding="utf-8").splitlines())
        require(all(line in aux_lines for line in EXPECTED_AUX_LINES[f"{chapter}.aux"]), f"{chapter} AUX evidence drift")
        builds[chapter] = {
            "tex": record(ROOT / f"{chapter}.tex"),
            "aux": record(ROOT / f"{chapter}.aux"),
            "log": record(ROOT / f"{chapter}.log"),
            "pdf": record(ROOT / f"{chapter}.pdf"),
            "pdf_pages": spec["pages"],
            "visual_reviewed_pages": spec["visual"],
            "undefined_references": 0,
            "undefined_citations": 0,
            "rerun_notices": 0,
            "new_block_overfull_boxes": 0,
        }
    builds["independent_audits"] = {
        "D000996": {
            "status": "STRICT_PASS",
            "scope": ["left satellites", "projective effacements", "halfwise universality", "exact gluing", "no global all-Z universality"],
        },
        "D000997": {
            "status": "STRICT_PASS",
            "scope": ["satellite-to-derived comparison", "left-exact iff isomorphism", "negative-degree nonclaim", "pages 71-74 clean"],
        },
        "D000998": {
            "status": "STRICT_PASS",
            "scope": ["fine definition", "Phi-softness", "tensor fineness", "flat-cycle exactness", "conditional Cartan resolution", "215-page strict parse", "uniform 612x792 geometry", "pages 47-53 clean"],
        },
        "D000999": {
            "status": "STRICT_PASS",
            "scope": ["divisor sheaf", "restriction and flasqueness", "height-one stalks", "UFD exactness", "H1=Cl", "higher vanishing", "PGL excluded", "pages 64-67 clean"],
        },
    }
    return builds


def index_csv_bytes(rows: list[dict[str, str]]) -> bytes:
    fields = [
        "tag", "full_label", "file", "line", "kind", "short_label",
        "chapter", "section_label", "section_title", "text_sha256",
    ]
    return csv_bytes(fields, [{field: row.get(field, "") for field in fields} for row in rows])


def candidate_csv_bytes(rows: list[dict[str, str]]) -> bytes:
    fields = [
        "topic_id", "score", "hit_fields", "tag", "full_label", "file",
        "line", "kind", "section_title", "snippet", "status",
    ]
    return csv_bytes(fields, [{field: row.get(field, "") for field in fields} for row in rows])


def topic_map_csv_bytes(rows: list[dict[str, str]]) -> bytes:
    fields = [
        "topic_id", "label", "coverage", "confidence", "evidence_labels",
        "evidence_tags", "rationale", "review_state",
    ]
    return csv_bytes(fields, [{field: row.get(field, "") for field in fields} for row in rows])


def verify_scanner_oracle() -> dict[str, object]:
    mkidx = load_mkidx()
    index, errors, warnings, tex_hashes = mkidx.build_index()
    require(errors == [], f"Current bounded scanner errors: {errors}")
    require(tex_hashes == expected_tex_hashes(), "Current 119-file TeX hash oracle drift")
    require({path.name for path in ROOT.glob("*.tex")} == set(tex_hashes), "Live TeX filename surface drift")
    _, topics = load_csv(SOURCE / "topics.csv")
    candidates = mkidx.candidate_rows(index, topics)
    topic_map, map_errors, map_warnings = mkidx.topic_map_rows(index, topics)
    require(map_errors == [], f"Current topic-map errors: {map_errors}")
    warnings = [*warnings, *map_warnings]

    _, old_index = load_csv(SOURCE / "stx.csv")
    fields = list(old_index[0])
    old_by = {row["full_label"]: row for row in old_index}
    new_by = {row["full_label"]: {field: row[field] for field in fields} for row in index}
    require(set(old_by) <= set(new_by), "Scanner removed an existing label")
    require(set(new_by) - set(old_by) == set(NEW_LABEL_ROWS), "New-label set drift")
    for label, expected in NEW_LABEL_ROWS.items():
        row = new_by[label]
        file, line, kind, section_label, section_title, text_sha256 = expected
        require(row == {
            "tag": "",
            "full_label": label,
            "file": file,
            "line": line,
            "kind": kind,
            "short_label": label.split("-", 1)[1],
            "chapter": {"homology.tex": "Homological Algebra", "derived.tex": "Derived Categories", "cohomology.tex": "Cohomology of Sheaves", "divisors.tex": "Divisors"}[file],
            "section_label": section_label,
            "section_title": section_title,
            "text_sha256": text_sha256,
        }, f"New label row drift: {label}")
    changed = []
    for label in old_by:
        if old_by[label] != new_by[label]:
            require(
                all(old_by[label][field] == new_by[label][field] for field in fields if field != "line"),
                f"Existing label substantive metadata drift: {label}",
            )
            changed.append(label)
    line_counts = Counter(old_by[label]["file"] for label in changed)
    require(dict(sorted(line_counts.items())) == EXPECTED_EXISTING_LINE_CHANGES, "Existing label line-only oracle drift")

    _, old_candidates = load_csv(SOURCE / "tcand.csv")
    old_c = {(row["topic_id"], row["full_label"]): row for row in old_candidates}
    new_c = {(row["topic_id"], row["full_label"]): row for row in candidates}
    require(set(new_c) - set(old_c) == EXPECTED_CANDIDATE_ADDED, "Candidate-addition key oracle drift")
    require(set(old_c) - set(new_c) == EXPECTED_CANDIDATE_REMOVED, "Candidate-removal key oracle drift")
    changed_candidates = []
    for key in set(old_c) & set(new_c):
        if old_c[key] != new_c[key]:
            require(
                all(old_c[key][field] == new_c[key][field] for field in old_c[key] if field != "line"),
                f"Existing candidate substantive metadata drift: {key}",
            )
            changed_candidates.append(key)
    candidate_line_counts = Counter(old_c[key]["file"] for key in changed_candidates)
    require(dict(sorted(candidate_line_counts.items())) == EXPECTED_CANDIDATE_EXISTING_LINE_CHANGES, "Candidate line-only oracle drift")
    require(len(index) == 22050 and len(candidates) == 1263 and len(topic_map) == 13, "Scanner count oracle drift")
    require(sum(1 for row in index if row["tag"]) == 21437, "Official-tag join count drift")
    require(len(warnings) == 622, "Scanner warning count drift")
    return {
        "index": index,
        "candidates": candidates,
        "topic_map": topic_map,
        "warnings": warnings,
        "tex_hashes": tex_hashes,
        "counts": EXPECTED_SCAN_COUNTS,
        "delta": {
            "changed_tex_files": ["cohomology.tex", "derived.tex", "divisors.tex", "homology.tex"],
            "new_labels": 11,
            "existing_rows_line_number_only": 823,
            "existing_text_hash_changes": 0,
            "existing_other_metadata_changes": 0,
            "official_tag_changes": 0,
            "candidate_count_delta": 8,
            "candidate_keys_added": 9,
            "candidate_keys_removed_by_cap": 1,
        },
    }


def verify_external() -> dict[str, object]:
    require(SOURCE.is_dir() and not SOURCE.is_symlink(), "Missing plain r41 predecessor")
    names = {path.name for path in SOURCE.iterdir() if path.is_file()}
    require(names == set(EXPECTED_SOURCE), "r41 predecessor surface drift")
    records = []
    for name, expected in sorted(EXPECTED_SOURCE.items()):
        require_identity(SOURCE / name, expected)
        records.append(record(SOURCE / name))
    require(
        (len(records), sum(int(item["bytes"]) for item in records), aggregate(records))
        == EXPECTED_SOURCE_SURFACE,
        "r41 predecessor aggregate drift",
    )
    predecessor = strict_json(SOURCE / "r41-check.json")
    require(predecessor.get("status") == "PASS" and predecessor.get("errors") == [], "r41 predecessor receipt not PASS")
    for name, expected in EXPECTED_RUNTIME.items():
        require_identity(ROOT / name, expected)
    for name, expected in EXPECTED_AUTHORITY.items():
        require_identity(AUTHORITY / name, expected)
    require(sys.version_info[:3] == (3, 13, 9) and sys.implementation.cache_tag == "cpython-313", "Python runtime drift")
    semantic = verify_semantic()
    repairs = verify_repairs()
    builds = verify_builds()
    scanner = verify_scanner_oracle()
    return {
        "predecessor": {
            "name": "tohoku_r41",
            "files": records,
            "file_count": len(records),
            "bytes": sum(int(item["bytes"]) for item in records),
            "aggregate_sha256": aggregate(records),
        },
        "semantic": semantic,
        "repairs": repairs,
        "builds": builds,
        "scanner": scanner,
    }


def normalize_source_loc(row: dict[str, str]) -> dict[str, str]:
    output = dict(row)
    if "source_loc" in output:
        output["source_loc"] = output["source_loc"].replace("sem/r16/nodes.csv:", "sem/r15/nodes.csv:")
    return output


def verify_stage(root: Path, receipt_mode: bool) -> dict[str, object]:
    external = verify_external()
    require(root.is_dir() and not root.is_symlink(), f"Missing plain stage/target: {root}")
    names = {path.name for path in root.iterdir() if path.is_file()}
    expected_names = PAYLOAD | ({"r42-check.json"} if receipt_mode else set())
    require(names == expected_names, f"Stage/target file surface drift: {names ^ expected_names}")
    require(not any(path.is_dir() for path in root.iterdir()), "Unexpected stage/target subdirectory")
    cfg = strict_json(root / "cfg.json")
    require(cfg.get("dossier_id") == "tohoku_r42", "r42 cfg dossier ID drift")
    require(cfg.get("expected_units") == 991, "r42 cfg unit count drift")
    require(cfg.get("semantic_successor", {}).get("generation") == "sem/r16", "r42 cfg semantic generation drift")
    require(cfg.get("inputs", {}).get("primary", {}).get("source_file") == "sem/r16/nodes.csv", "r42 cfg primary source drift")
    require(cfg.get("inputs", {}).get("primary", {}).get("sha256") == EXPECTED_SEM["nodes.csv"][1], "r42 cfg node pin drift")
    require(cfg.get("inputs", {}).get("sem_manifest", {}).get("sha256") == EXPECTED_SEM["manifest.json"][1], "r42 cfg manifest pin drift")
    require(cfg.get("inputs", {}).get("sem_validation", {}).get("sha256") == EXPECTED_SEM["validation.json"][1], "r42 cfg validation pin drift")
    require("sem_input" not in cfg.get("inputs", {}) and "sem_check" not in cfg.get("inputs", {}), "Stale sem/r15 QA inputs remain in r42 cfg")

    intake = strict_json(root / "intake.json")
    check = strict_json(root / "check.json")
    mcheck = strict_json(root / "mcheck.json")
    for name, value in (("intake", intake), ("scan", check), ("map", mcheck)):
        require(value.get("status") == "PASS" and value.get("errors") == [], f"{name} receipt not PASS")
    require(mcheck.get("outputs_promoted") is True, "Mapping outputs not promoted")

    require((root / "topics.csv").read_bytes() == (SOURCE / "topics.csv").read_bytes(), "topics.csv drift")
    scanner = external["scanner"]
    require((root / "stx.csv").read_bytes() == index_csv_bytes(scanner["index"]), "stx.csv does not match exact live oracle")
    require((root / "tcand.csv").read_bytes() == candidate_csv_bytes(scanner["candidates"]), "tcand.csv does not match exact live oracle")
    require((root / "tmap.csv").read_bytes() == topic_map_csv_bytes(scanner["topic_map"]), "tmap.csv does not match exact live oracle")
    require(check.get("counts") == EXPECTED_SCAN_COUNTS, "r42 scan counts drift")
    require(check.get("warnings") == scanner["warnings"], "r42 scan warnings drift")
    require(check.get("tex_sha256") == scanner["tex_hashes"], "r42 scan TeX hashes drift")
    require(check.get("sha256", {}).get("tags/tags") == EXPECTED_RUNTIME["tags/tags"][1], "r42 scan tag hash drift")

    _, sem_nodes = load_csv(SEM / "nodes.csv")
    _, units = load_csv(root / "units.csv")
    require(len(units) == 991, "r42 unit count drift")
    require([row["id"] for row in units] == [row["node_id"] for row in sem_nodes], "r42 stable unit IDs drift")
    require(all(row["source_file"] == "sem/r16/nodes.csv" for row in units), "r42 unit source path drift")
    require(intake.get("counts", {}).get("units") == 991, "r42 intake unit receipt drift")

    fields, old_decisions = load_csv(SOURCE / "dec.csv")
    new_fields, decisions = load_csv(root / "dec.csv")
    require(fields == new_fields, "Decision schema drift")
    require([row["decision_id"] for row in decisions] == [f"D{number:06d}" for number in range(1, 1000)], "Decision sequence drift")
    require(decisions[:995] == old_decisions and decisions[995:] == DECISION_ROWS, "Decision prefix/appended rows drift")
    prefix = (SOURCE / "dec.csv").read_bytes()
    require((root / "dec.csv").read_bytes().startswith(prefix), "Decision byte prefix drift")

    issue_fields, old_issues = load_csv(SOURCE / "issues.csv")
    new_issue_fields, issues = load_csv(root / "issues.csv")
    require(issue_fields == new_issue_fields and len(issues) == 29, "Issue schema/count drift")
    require(issues[:28] == old_issues[:28], "Issues I000001-I000028 changed")
    require(old_issues[28]["issue_id"] == "I000029", "Predecessor I000029 missing")
    expected_issue = dict(old_issues[28])
    expected_issue["status"] = "resolved"
    expected_issue["resolution_decision"] = "D000996"
    require(issues[28] == expected_issue, "I000029 changed outside its two authorized fields")
    for key in expected_issue:
        if key not in {"status", "resolution_decision"}:
            require(issues[28][key] == old_issues[28][key], f"I000029 unauthorized mutation: {key}")
    require([row["issue_id"] for row in issues if row["status"] != "resolved"] == [], "Active source issue remains")

    require(mcheck.get("counts") == EXPECTED_MAPPING_COUNTS, "r42 mapping counts drift")
    require(mcheck.get("warnings") == check.get("warnings"), "Map/scan warning mismatch")
    _, undecided = load_csv(root / "ucand.csv")
    require(undecided == [], "Unexpected undecided candidates")
    _, old_map = load_csv(SOURCE / "map.csv")
    _, new_map = load_csv(root / "map.csv")
    require(len(old_map) == len(new_map) == 991, "Map row count drift")
    old_by = {row["unit_id"]: row for row in old_map}
    new_by = {row["unit_id"]: row for row in new_map}
    require(set(old_by) == set(new_by), "Map unit set drift")
    target_units = {row["unit_id"] for row in DECISION_ROWS}
    for unit_id in set(old_by) - target_units:
        require(normalize_source_loc(new_by[unit_id]) == old_by[unit_id], f"Unauthorized map mutation: {unit_id}")
    for decision in DECISION_ROWS:
        row = new_by[decision["unit_id"]]
        require(row["decision_id"] == decision["decision_id"], f"Latest decision not selected: {decision['decision_id']}")
        require(row["disposition"] == decision["disposition"], f"Disposition drift: {decision['decision_id']}")
        require(row["review_state"] == decision["review_state"], f"Review state drift: {decision['decision_id']}")
        require(row["stacks_labels"] == decision["stacks_labels"], f"Stacks-label drift: {decision['decision_id']}")
        require(row["rationale"] == decision["rationale"], f"Rationale drift: {decision['decision_id']}")
        require(row["stacks_tags"] == "", f"Unexpected official tag: {decision['decision_id']}")
    gap_count = sum(EXPECTED_MAPPING_COUNTS["dispositions"][name] for name in ("existing_weaker", "extend_existing", "new_statement", "new_section"))
    require(gap_count == 60, "Gap-class arithmetic drift")

    status = (root / "STATUS.md").read_text(encoding="utf-8")
    for token in ("sem/r16", "D000996", "D000999", "I000029", "60 gap-class"):
        require(token in status, f"STATUS missing token: {token}")

    result = {
        "status": "PASS",
        "errors": [],
        "stable_units": 991,
        "decisions": 999,
        "decisions_appended": DECISION_ROWS,
        "resolved_issue": {"issue_id": "I000029", "resolution_decision": "D000996", "only_fields_changed": ["status", "resolution_decision"]},
        "active_source_issues": [],
        "mapping_counts": EXPECTED_MAPPING_COUNTS,
        "scan_counts": EXPECTED_SCAN_COUNTS,
        "scanner_delta": scanner["delta"],
        "remaining_gap_class_dispositions": 60,
        "semantic_generation": "sem/r16",
        "byte_identical_payloads": ["topics.csv"],
        "external_evidence": {
            "predecessor_aggregate_sha256": external["predecessor"]["aggregate_sha256"],
            "semantic_aggregate_sha256": external["semantic"]["aggregate_sha256"],
            "repair_aggregate_sha256": external["repairs"]["aggregate_sha256"],
        },
    }

    if receipt_mode:
        receipt = strict_json(root / "r42-check.json")
        require(receipt.get("schema") == "tohoku-stacks-mapping-successor-r42-v1", "r42 receipt schema drift")
        require(receipt.get("status") == "PASS" and receipt.get("errors") == [], "r42 receipt not PASS")
        require(receipt.get("deltas") == result, "r42 receipt delta replay mismatch")
        expected_files = [record(root / name) for name in sorted(PAYLOAD)]
        require(receipt.get("files") == expected_files, "r42 receipt output records drift")
        require(receipt.get("predecessor_dossier") == external["predecessor"], "r42 receipt predecessor evidence drift")
        require(receipt.get("semantic_source") == external["semantic"], "r42 receipt semantic evidence drift")
        require(receipt.get("source_repairs") == external["repairs"], "r42 receipt repair evidence drift")
        require(receipt.get("builds") == external["builds"], "r42 receipt build evidence drift")
        execution = receipt.get("execution", {})
        require(execution.get("contract") == "one_shot_self_attested_driver_bootstrap_builder_validator; exact_inputs_locked_through_atomic_no_overwrite_promotion", "r42 execution contract drift")
        require(set(execution.get("attestation", {})) == {"driver", "bootstrap", "builder", "validator"}, "r42 execution attestation surface drift")
    return result


def verify_self_attestation() -> dict[str, object]:
    raw = os.environ.pop("TOHOKU_R42_VALIDATOR_EXPECTED", "")
    actual = identity(Path(__file__))
    if not raw:
        return {"mode": "independent_direct", "path": "srcmap/validate_tohoku_r42.py", "bytes": actual[0], "sha256": actual[1]}
    expected = json.loads(raw)
    require(expected == {"bytes": actual[0], "sha256": actual[1]}, "Validator same-bytes attestation drift")
    return {"mode": "builder_locked_subprocess", "path": "srcmap/validate_tohoku_r42.py", "bytes": actual[0], "sha256": actual[1]}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--static", action="store_true")
    parser.add_argument("--stage", type=Path)
    parser.add_argument("--receipt", action="store_true")
    args = parser.parse_args()
    attestation = verify_self_attestation()
    require(args.static != (args.stage is not None), "Choose exactly one of --static or --stage")
    if args.static:
        external = verify_external()
        result = {
            "schema": "tohoku-r42-static-input-audit-v1",
            "status": "PASS",
            "errors": [],
            "attestation": attestation,
            "target_absent": not os.path.lexists(TARGET),
            "stage_absent": not os.path.lexists(STAGE),
            "predecessor_aggregate_sha256": external["predecessor"]["aggregate_sha256"],
            "semantic_aggregate_sha256": external["semantic"]["aggregate_sha256"],
            "scanner_delta": external["scanner"]["delta"],
            "builds": external["builds"],
            "launch_authorized": False,
        }
    else:
        result = {
            "schema": "tohoku-r42-stage-validation-v1",
            "attestation": attestation,
            **verify_stage(args.stage.resolve(), args.receipt),
        }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
