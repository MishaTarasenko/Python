import unittest
from app.io import output, input


class TestInput(unittest.TestCase):
    def test_read_file_builtin_file_not_found(self):
        """
            Test if file was not found
        """
        with self.assertRaises(FileNotFoundError):
            input.input_text_from_file("not_found.txt")

    def test_read_file(self):
        """
            Test that the read text will be the same as when it was written
        """
        result = input.input_text_from_file("../../data/test1.txt")
        self.assertIsNot(result, None)

    def test_write_and_read_file(self):
        """
            Test that the read text will be the same as when it was written
        """
        test_data = "test text"
        output.output_to_file("../../data/test2.txt", test_data)
        result = input.input_text_from_file("../../data/test2.txt")
        self.assertEqual(result, test_data)

    def test_read_file_builtin_file_not_found_pandas(self):
        """
            Test if file was not found
        """
        with self.assertRaises(FileNotFoundError):
            input.input_text_with_pandas("../../not_found.txt")

    def test_read_file_pandas(self):
        """
            Test that the read text will be the same as when it was written
        """
        result = input.input_text_with_pandas("../../data/test_panda.csv")
        self.assertIsNot(result, None)

    def test_write_and_read_file_pandas(self):
        """
            Test that the read text will be the same as when it was written
        """
        test_data = "test text"
        output.output_to_file_with_pandas("../../data/test_pandas_2.csv", test_data)
        result = input.input_text_with_pandas("../../data/test_pandas_2.csv")
        self.assertEqual(result, test_data)
