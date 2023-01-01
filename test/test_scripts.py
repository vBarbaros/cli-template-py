import unittest
from pathlib import Path
import os, sys

parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)


class ScriptsTest(unittest.TestCase):
    def setUp(self):
        self.api_calls_file_path = os.path.join(parentdir, 'src/scripts', 'api_calls.py')
        self.io_ops_file_path = os.path.join(parentdir, 'src/scripts', 'io_ops.py')

    def test_api_calls_file(self):
        print("\nRUNNING TESTS FOR ../scripts/ dir - api_calls.py")
        print("Ensure api_calls.py file exists")
        self.assertEqual(os.path.isfile(self.api_calls_file_path), True)
        print("OK")

    def test_io_ops_file(self):
        print("\nRUNNING TESTS FOR ../scripts/ dir - io_ops.py")
        print("Ensure io_ops.py file exists")
        self.assertEqual(os.path.isfile(self.io_ops_file_path), True)
        print("OK")


if __name__ == '__main__':
    unittest.main()
