import unittest
from collections import namedtuple
from uva10267 import Editor


Case = namedtuple("Case", "cmds want")


class EditorTest(unittest.TestCase):
    def setUp(self):
        self.editor = Editor()

    def runCases(self, cases):
        for i, case in enumerate(cases):
            with self.subTest(subtest=i):
                for cmd in case.cmds:
                    self.editor.command(cmd)
                self.assertEqual(self.editor.dump(), case.want)

    def test_Create_new_image(self):
        test_cases = [
            ("I 1 1", [["O"]]),
            ("I 1 2", [["O"], ["O"]]),
            ("I 2 1", [["O", "O"]]),
            ("I 2 2", [["O", "O"], ["O", "O"]]),
            ("I 51 72", [["O"] * 51 for _ in range(72)]),
        ]
        for cmd, want in test_cases:
            with self.subTest():
                self.editor.command(cmd)
                self.assertEqual(self.editor.dump(), want)

    def test_Color_pixel_and_clear_image(self):
        cases = [
            Case(cmds=["I 1 1", "L 1 1 Z", "C"], want=[["O"]]),
            Case(cmds=["I 1 2", "L 1 2 Z", "C"], want=[["O"], ["O"]]),
            Case(
                cmds=["I 10 80", "L 5 4 A", "C"],
                want=[["O"] * 10 for _ in range(80)],
            ),
        ]
        self.runCases(cases)

    def test_Draw_vertical_segment(self):
        cases = [
            Case(cmds=["I 1 1", "V 1 1 1 B"], want=[["B"]]),
            Case(cmds=["I 1 2", "V 1 1 1 B"], want=[["B"], ["O"]]),
            Case(cmds=["I 1 2", "V 1 2 2 B"], want=[["O"], ["B"]]),
            Case(cmds=["I 1 2", "V 1 1 2 B"], want=[["B"], ["B"]]),
            Case(
                cmds=["I 2 2", "V 1 1 2 B"],
                want=[["B", "O"], ["B", "O"]],
            ),
            Case(
                cmds=["I 2 2", "V 1 2 1 B"],
                want=[["B", "O"], ["B", "O"]],
            ),
            Case(
                cmds=["I 2 3", "V 2 2 3 B"],
                want=[["O", "O"], ["O", "B"], ["O", "B"]],
            ),
        ]
        self.runCases(cases)

    def test_Draw_filled_rectangle(self):
        Case = namedtuple("Case", "cmds want")
        cases = [
            Case(cmds=["I 1 1", "K 1 1 1 1 B"], want=[["B"]]),
            Case(cmds=["I 1 2", "K 1 1 1 1 B"], want=[["B"], ["O"]]),
            Case(cmds=["I 1 2", "K 1 1 1 2 B"], want=[["B"], ["B"]]),
            Case(cmds=["I 1 2", "K 1 2 1 1 B"], want=[["O"], ["O"]]),
            Case(
                cmds=["I 2 2", "K 1 1 1 2 B"],
                want=[["B", "O"], ["B", "O"]],
            ),
            Case(
                cmds=["I 2 2", "K 1 1 2 1 B"],
                want=[["B", "B"], ["O", "O"]],
            ),
            Case(
                cmds=["I 2 2", "K 2 1 2 1 B"],
                want=[["O", "B"], ["O", "O"]],
            ),
            Case(
                cmds=["I 2 2", "K 2 1 1 1 B"],
                want=[["O", "O"], ["O", "O"]],
            ),
            Case(
                cmds=["I 2 2", "K 2 2 1 1 B"],
                want=[["O", "O"], ["O", "O"]],
            ),
            Case(
                cmds=["I 2 3", "K 1 2 2 3 B"],
                want=[["O", "O"], ["B", "B"], ["B", "B"]],
            ),
            Case(
                cmds=["I 2 3", "K 2 3 1 2 B"],
                want=[["O", "O"], ["O", "O"], ["O", "O"]],
            ),
            Case(
                cmds=["I 2 3", "K 2 2 2 3 B"],
                want=[["O", "O"], ["O", "B"], ["O", "B"]],
            ),
        ]
        self.runCases(cases)


if __name__ == "__main__":
    unittest.main()
