#!/usr/bin/python3
"""Creates unittests for models/base_model.py.
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_no_args_instantiation(self):
        self.assertEqual(BaseModel, type(BaseModel()))


if __name__ == "__main__":
    unittest.main()
