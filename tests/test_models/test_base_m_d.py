#!/usr/bin/python3
""" The test base module for testing the base_model module """
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """the class to test the basemodel class """
    
    def setUp():
        self.model1 = BaseModel()
        self.model2 = BaseModel()

    def test_dict(self):
        """testing the to_dict() method of the basemodel class"""
        
        self.assertIsInstance(self.model1.to_dict(), dict)
        self.assertIsInstance(self.model2.to_dict(), dict)

