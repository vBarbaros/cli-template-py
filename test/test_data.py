import unittest
from pathlib import Path
import os, sys

parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)


class ScriptsTest(unittest.TestCase):
    def setUp(self):
        self.input_file_path = os.path.join(parentdir, 'src/data', 'input.txt')
        self.out_file_path = os.path.join(parentdir, 'src/data', 'out.txt')

    def test_input_file(self):
        print("\nRUNNING TESTS FOR ../data/ dir - input.txt")
        print("Ensure input.txt file exists")
        self.assertEqual(os.path.isfile(self.input_file_path), True)
        print("OK")

    def test_out_file(self):
        print("\nRUNNING TESTS FOR ../scripts/ dir - out.txt")
        print("Ensure out.txt file exists")
        self.assertEqual(os.path.isfile(self.out_file_path), True)
        print("OK")


if __name__ == '__main__':
    unittest.main()
