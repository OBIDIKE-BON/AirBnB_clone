#!/usr/bin/python3
"""The module state which has the state class"""
from models.base_model import BaseModel


class State(BaseModel):
    """The class state which inherits from the basemodel class"""

    name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
