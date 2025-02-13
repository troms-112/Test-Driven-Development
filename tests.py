import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    def test1(self):
        """
        test to check if an empty string is correctly rejected

        :return: False
        """
        self.assertFalse(check_pwd(""))

if __name__ == "__main__":
    unittest.main()