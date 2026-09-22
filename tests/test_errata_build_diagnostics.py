import sys
from pathlib import Path
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from build_r49_chapter import diagnostics

class DiagnosticsTests(unittest.TestCase):
    def test_font_dump_is_not_error(self):
        self.assertEqual(diagnostics('Overfull \\hbox (1pt too wide)\n! [][]\\OT1/lmr/m/n/10 text\n')['fatal_duplicate_glyph_rerun'], [])
    def test_actual_errors_remain_fatal(self):
        text='! Undefined control sequence.\n! LaTeX Error: Missing begin document.\nMissing character: x\nRerun to get cross-references right.\n'
        self.assertEqual(len(diagnostics(text)['fatal_duplicate_glyph_rerun']), 4)
    def test_other_exclamation_not_exempt(self):
        self.assertEqual(diagnostics('! [][] is an error\n')['fatal_duplicate_glyph_rerun'], ['! [][] is an error'])

if __name__=='__main__':unittest.main()
