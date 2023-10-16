#!/usr/bin/python3
"""Creates unittests for models/user.py.
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))


if __name__ == "__main__":
    unittest.main()
