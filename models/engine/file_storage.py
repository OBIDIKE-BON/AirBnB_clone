#!/usr/bin/python3
""" This is a module with the FileStorage class that
serializes instances to a JSON file and deserializes
JSON file to instances
"""
import json


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
        self.__objects[f"{name}.{obj_id}"] = obj.to_dict()

    def save(self):
        """serializes the objects in __objects"""
        with open(self.__file_path, 'w', encoding='utf8') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf8') as f:
                self.__objects = json.load(f)
                return self.__objects
        except Exception:
            return self.__objects
