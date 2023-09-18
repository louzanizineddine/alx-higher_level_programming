#!/usr/bin/python3

""" BASE MODULE HAS ONE CLASS BASE """

import json
import os


class Base:
    """class base has one private attribute"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor method for the base class"""
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """list of dics to json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save a list of square or rectangle to a file"""

        filename = cls.__name__ + ".json"
        list_dic = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_dic))

    @staticmethod
    def from_json_string(json_string):
        """from json string to dictionary"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create an instance """
        if cls.__name__ == "Rectangle":
            rec = cls(10, 10)
        else:
            rec = cls(10)
        rec.update(**dictionary)
        return rec

    @classmethod
    def load_from_file(cls):
        """ Return all instances of class been saved in file"""
        file = "{}.json".format(cls.__name__)

        if os.path.exists(file) is False:
            return []

        with open(file, 'r') as f:
            list_str = f.read()

        classes_list = cls.from_json_string(list_str)
        instances_list = []

        for index in range(len(classes_list)):
            instances_list.append(cls.create(**classes_list[index]))

        return instances_list
