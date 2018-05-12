# -*- coding: utf-8 -*-

from api_ary_gen import ApiAryGen
from django_rest_api_gen import DjangoRestApiGen
from behave_gen import BehaveGen
from argument import Argument


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

        arguments_in_path = [argument for argument in self.arguments if argument.location == Argument.IN_PATH]
        arguments_in_query = [argument for argument in self.arguments if argument.location == Argument.IN_QUERY]
        arguments_in_body = [argument for argument in self.arguments if argument.location == Argument.IN_BODY]
        parameters['all_arguments'] = self.arguments
        parameters['arguments_in_path'] = arguments_in_path
        parameters['arguments_in_query'] = arguments_in_query
        parameters['arguments_in_body'] = arguments_in_body
        # TODO: Ta assumindo que so existe uma chave de busca e que eh sempre o 1o campo.
        # key = self.arguments[0]
        # parameters['key_name'] = key.get_name()
        # parameters['key_type'] = key.get_type()
        # parameters['key_sample'] = key.get_sample()
        # parameters['key_description'] = key.get_description()
        # TODO: acho que devo passar todos os argumentos, identificando a localizacao deles.
        # TODO: Assim os templates iteram e selecionam o que for necessario.
        # TODO: Talvez, para facilitar, eu passo todos, mas tb separo por path, query e body.
        # properties = []
        # for argument in self.arguments[1:]:
        #     properties.append(argument)
        # parameters['properties'] = properties
        self.doc.gen(parameters)
        self.route_code.gen(parameters)
        self.bdd_code.gen(parameters)
