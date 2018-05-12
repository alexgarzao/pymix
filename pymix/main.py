# -*- coding: utf-8 -*-

from endpoint_gen import EndpointGen
from argument import Argument


if __name__ == '__main__':
    # TODO: Implementar testes com behave
    # Teste 1: pymix api-rest new-method cep cep_route number:string id_estado:int id_cidade:int id_bairro:int
    e1 = EndpointGen()
    e1.entity = 'cep'
    e1.route = 'cep_route'
    e1.add_argument(Argument('number', Argument.STRING, Argument.IN_PATH))
    e1.add_argument(Argument('id_estado', Argument.INT, Argument.IN_BODY))
    e1.add_argument(Argument('id_cidade', Argument.INT, Argument.IN_BODY))
    e1.add_argument(Argument('id_bairro', Argument.INT, Argument.IN_BODY))
    e1.gen()

    # Teste 2: pymix api-rest new-method estado id:int id_cidade:int id_bairro:int sigla:string nome:string

    # Teste 3: pymix api-rest new-method cidade id:int id_bairro:int nome:string

    # Teste 4: pymix api-rest new-method bairro id:int nome:string

    # TODO: parametros podem estar no path, na query ou no body.
    # TODO: Isso deve ficar definido quando um argumento eh adicionado.
    # TODO: Por enquanto vou assumir que o 1o eh o que fica no path.
