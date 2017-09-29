# -*- coding: utf-8 -*-

class Argument(object):
    INT = 0
    STRING = 1

    def __init__(self, name=None, type=None):
        self.name = name
        self.type = type

    def get_name(self):
        return self.name

    def get_type(self):
        str_types = ['number', 'string']
        return str_types[self.type]

    def get_sample(self):
        sample_types = ['123', 'ABCDE']
        return sample_types[self.type]

    def get_description(self):
        return 'Descricao: TODO'
