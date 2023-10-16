#!/usr/bin/python3
"""The module amenity which has the amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """The class user which inherits from the basemodel class"""

    name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
