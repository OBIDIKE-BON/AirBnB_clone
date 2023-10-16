#!/usr/bin/python3
"""The module city which has the city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """The class city which inherits from the basemodel class"""

    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
