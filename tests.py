import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    def test1(self):
        """
        test to check if an empty string is correctly rejected

        :return: False
        """
        self.assertFalse(check_pwd(""))

    def test2(self):
        """
        test checks if passwords with less than 8 characters are rejected

        :return: False
        """
        self.assertFalse(check_pwd("A2sghj+"))

if __name__ == "__main__":
    unittest.main()