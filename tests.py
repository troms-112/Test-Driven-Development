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

    def test3(self):
        """
        test checks if passwords greater than 20 character are rejected

        :return: False
        """
        self.assertFalse(check_pwd("a2Aaaaaaaaaaaaaa+aaaaaa!22"))

    def test4(self):
        """
        test checks if passwords contain at least one lower case letter
        (standard English alphabet)

        :return: False
        """
        self.assertFalse(check_pwd("A2AA2A2A"))

    def test5(self):
        """
        test checks if password contain at least one upper case letter
        (standard English alphabet)

        :return: False
        """
        self.assertFalse(check_pwd("a3a3a3a3a3"))

    def test6(self):
        """
        test checks if password contains at least one digit

        :return: False
        """
        self.assertFalse(check_pwd("aAaAaDDF"))

    def test7(self):
        """
        test checks if password contains at least one of the following symbols
        ~`!@#$%^&*()_+-=

        :return: False
        """
        self.assertFalse(check_pwd("a2FF3gdsa"))


if __name__ == "__main__":
    unittest.main()