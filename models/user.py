#!/usr/bin/python3
"""The module user which has the user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """The class user which inherits from the basemodel class"""

    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self):
        BaseModel.__init__(self)
