import unittest
from pathlib import Path
import os, sys

parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)


class SrcTest(unittest.TestCase):
    def setUp(self):
        self.dialog_file_path = os.path.join(parentdir, 'src', 'run.py')

    def test_run_file(self):
        print("\nRUNNING TESTS FOR ../src/ dir - run.py")
        print("Ensure run.py file exists")
        self.assertEqual(os.path.isfile(self.dialog_file_path), True)
        print("OK")


if __name__ == '__main__':
    unittest.main()
