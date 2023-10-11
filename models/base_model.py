#!/usr/bin/python3
""" This defines the base model class for hbnb """
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """ This is the basemodel class for hbnb """

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            kwargs['created_at'] = datetime.fromisoformat(kwargs['created_at'])
            kwargs['updated_at'] = datetime.fromisoformat(kwargs['updated_at'])
            self.__dict__.update(kwargs)
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    pass
                else:
                    self.__dict__[k] = v
            self.__dict__.pop('__class__')
        else:
            storage.new(self)

    def __str__(self):
        """The string representation of the BaseModel instance """
        return f"{[BaseModel.__name__]} ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public attribute updated_at to the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        my_dict = dict(self.__dict__)
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
