#!/usr/bin/python3
""" The test base module for testing the base_model module """
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """the class to test the basemodel class """
    
    def setUp():
        self.model1 = BaseModel()
        self.model2 = BaseModel()

    def test_uuid(self):
        """testing the id attribute of the basemodel class"""
        
        self.assertTrue(hasattr(self.model1, "id"))
        self.assertIsInstance(self.model1, BaseModel)
        self.assertNotEqual(self.model1.id, model2.id)
        self.assertIsInstance(self.model2.id, str)

    def test_datetime(self):
        """testing the created_at and updated_at attributes"""

        self.assertTrue(hasattr(self.model1, "created_at"))
        self.assertTrue(hasattr(self.model1, "updated_at"))
        self.assertTrue(hasattr(self.model2, "created_at"))
        self.assertTrue(hasattr(self.model2, "updated_at"))
        self.assertIsInstance(self.model2.created_at, str)
        self.assertIsInstance(self.model1.updated_at, str)
        self.assertIsInstance(self.model1.created_at, str)
        self.assertIsInstance(self.model2.updated_at, str)

    def test_str(self):
        """test the string representation of the basemodel instance"""

        self.assertIsInstance(print(self.model1, str))
        self.assertIsInstance(print(self.model2, str)
