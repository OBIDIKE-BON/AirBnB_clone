#!/usr/bin/python3
"""The module review which has the review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """The class user which inherits from the basemodel class"""

    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
