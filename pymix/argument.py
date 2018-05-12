# -*- coding: utf-8 -*-

class Argument(object):
    # Types:
    INT = 0
    STRING = 1
    # Location:
    IN_PATH = 1
    IN_QUERY = 2
    IN_BODY = 3
    def __init__(self, name=None, type=None, location=None):
        self.name = name
        self.type = type
        self.location = location

    def get_name(self):
        return self.name

    def get_type(self):
        str_types = ['number', 'string']
        return str_types[self.type]

    def get_sample(self):
        sample_types = ['123', 'ABCDE']
        return sample_types[self.type]

    def get_description(self):
        return 'Descricao de %s: TODO' % self.name
