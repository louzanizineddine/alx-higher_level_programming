#!/usr/bin/python3

"""BASE MODULE HAS ONE CLASS BASE"""
import json

class Base:
    """class base has one private attribute"""
    
    __nb_objects = 0
    
    def __init__(self, id=None):
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
