#!/usr/bin/python3
"""Creates unittests for models/engine/file_storage.py.
"""
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Unittests to test instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)


if __name__ == "__main__":
    unittest.main()
