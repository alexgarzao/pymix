# -*- coding: utf-8 -*-

from api_ary_gen import ApiAryGen
from django_rest_api_gen import DjangoRestApiGen
from behave_gen import BehaveGen


class EndpointGen(object):

    def __init__(self):
        self.entity = 'None'
        self.route = 'None'
        self.arguments = []
        self.doc = ApiAryGen()
        self.route_code = DjangoRestApiGen()
        self.bdd_code = BehaveGen()

    def add_argument(self, argument):
        self.arguments.append(argument)

    def gen(self):
        parameters = {}
        parameters['entity_name'] = self.entity
        parameters['route'] = self.route

        # TODO: Ta assumindo que so existe uma chave de busca e que eh sempre o 1o campo.
        key = self.arguments[0]
        parameters['key_name'] = key.get_name()
        parameters['key_type'] = key.get_type()
        parameters['key_sample'] = key.get_sample()
        parameters['key_description'] = key.get_description()
        self.doc.gen(parameters)
        self.route_code.gen(parameters)
        self.bdd_code.gen(parameters)
