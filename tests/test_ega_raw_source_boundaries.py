"""Synthetic adverse cases for raw-source boundary validation."""
import unittest

from tools.ega_raw_source_boundaries import verify_numbered_span


SOURCE = (
    b"\\section{Example}\n\n"
    b"\\begin{env}[7.1.3]\n"
    b"\\label{I.7.1.3-fr}\n"
    b"The equivalence classes carry\n"
    b"a ring structure.\n"
    b"\\end{env}\n\n"
    b"An explicitly owned following proof.\n"
)


class RawSourceBoundaryTests(unittest.TestCase):
    def test_complete_unit(self):
        r = verify_numbered_span(SOURCE, 3, 7, "I.7.1.3-fr")
        self.assertEqual((r["begin_line"], r["label_line"], r["closing_line"]), (3, 4, 7))

    def test_separating_blanks_and_explicit_following_proof(self):
        r = verify_numbered_span(SOURCE, 2, 9, "I.7.1.3-fr")
        self.assertEqual(r["byte_offset_end_exclusive"], len(SOURCE))

    def test_truncated_final_assertion_and_closing_marker_rejected(self):
        for end in (4, 5, 6):
            with self.assertRaises(ValueError):
                verify_numbered_span(SOURCE, 3, end, "I.7.1.3-fr")

    def test_omitted_begin_rejected(self):
        with self.assertRaises(ValueError):
            verify_numbered_span(SOURCE, 4, 7, "I.7.1.3-fr")

    def test_previous_content_rejected(self):
        with self.assertRaises(ValueError):
            verify_numbered_span(SOURCE, 1, 7, "I.7.1.3-fr")

    def test_line_serialization_and_bounds(self):
        for raw, start, end in ((SOURCE.replace(b"\n", b"\r\n"), 3, 7),
                                (SOURCE[:-1], 3, 7), (SOURCE, 0, 7),
                                (SOURCE, 3, 99), (SOURCE, True, 7)):
            with self.assertRaises(ValueError):
                verify_numbered_span(raw, start, end, "I.7.1.3-fr")

    def test_duplicate_label_and_wrong_number_rejected(self):
        for raw in (SOURCE + b"\\label{I.7.1.3-fr}\n", SOURCE.replace(b"[7.1.3]", b"[7.1.2]")):
            with self.assertRaises(ValueError):
                verify_numbered_span(raw, 3, 7, "I.7.1.3-fr")

    def test_comment_cannot_close_environment(self):
        raw = SOURCE.replace(b"The equivalence classes carry", b"% \\end{env}\nThe equivalence classes carry")
        with self.assertRaises(ValueError):
            verify_numbered_span(raw, 3, 7, "I.7.1.3-fr")
        self.assertEqual(verify_numbered_span(raw, 3, 8, "I.7.1.3-fr")["closing_line"], 8)

    def test_unclosed_environment_rejected(self):
        with self.assertRaises(ValueError):
            verify_numbered_span(SOURCE.replace(b"\\end{env}", b""), 3, 9, "I.7.1.3-fr")


if __name__ == "__main__":
    unittest.main()
