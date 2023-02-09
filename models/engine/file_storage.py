#!/usr/bin/python3
"""
This module contains a class FileStorage that serializes
instanses to a JSON file and deserializes JSON file to
instances
"""
import json
import os.path
import sys
sys.path.append('/home/vagrant/AirBnB_clone/models')
from base_model_4 import BaseModel

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes
    JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary `objects` """
        return self.__objects

    def new(self, obj):
        """sets obj.id as key in dictionary(objects)"""
        key = obj["__class__"] + "." + obj["id"]
        self.__objects[key] = obj

    def save(self):
        """serializes the dictionary(objects) to the JSON file"""
        with open(self.__file_path, 'w') as json_file:
            json.dump(self.__objects, json_file)

    def reload(self):
        """deserializes JSON file to objects(dictionary)"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as json_file:
                self.__objects = json.load(json_file)

if __name__ == "__main__":
    
    """mod = BaseModel()
    mod2 = BaseModel()
    modjson = mod.to_dict()
    mod2json = mod2.to_dict()
    print("object mod created, mod.id: {}".format(mod.id))
    print("object mod2 created, mod2.id: {}".format(mod2.id))
    """
    file1 = FileStorage()
    """ print("file1 of type {} created".format(type(file1).__name__))
    file1.new(modjson)
    file1.new(mod2json)
    file1.save()"""
    file1.reload()
    print("{}".format(file1.all()))
