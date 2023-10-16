#!/usr/bin/python3
""" This is a module with the FileStorage class that
serializes instances to a JSON file and deserializes
JSON file to instances
"""
import json
# from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to JSON and also deserializes from JSON"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """adds an object into the dictionary __objects"""
        name = obj.__class__.__name__
        obj_id = obj.id
        self.__objects[f"{name}.{obj_id}"] = obj

    def save(self):
        """serializes the objects in __objects"""
        with open(self.__file_path, 'w', encoding='utf8') as f:
            objects = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf8') as f:
                objects = json.load(f)
                from models.base_model import BaseModel
                from models.user import User
                from models.place import Place
                from models.state import State
                from models.city import City
                from models.amenity import Amenity
                from models.review import Review

                for obj in objects.keys():
                    name = obj.split('.')
                    if name[0] == 'BaseModel':
                        self.__objects[obj] = BaseModel(**objects[obj])
                    elif name[0] == 'User':
                        self.__objects[obj] = User(**objects[obj])
                    elif name[0] == 'Place':
                        self.__objects[obj] = User(**objects[obj])
                    elif name[0] == 'State':
                        self.__objects[obj] = User(**objects[obj])
                    elif name[0] == 'City':
                        self.__objects[obj] = User(**objects[obj])
                    elif name[0] == 'Amenity':
                        self.__objects[obj] = User(**objects[obj])
                    elif name[0] == 'Review':
                        self.__objects[obj] = User(**objects[obj])

                return self.__objects
        except Exception as ep:
            return self.__objects
