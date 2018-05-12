# -*- coding: utf-8 -*-

from jinja2 import Template


TPL_ROUTE_DEFINITION = \
u'''## Rotas para criar/listar a entidade {{entity_name}} [/{{route}}/]

### Lista todas as entidades {{entity_name}} [GET]

+ Response 200 (application/json)
    + Attributes(array[{{entity_name}} response])

### Cria uma nova entidade {{entity_name}} [POST]

+ Request Cria {{entity_name}} (application/json)
    + Attributes({{entity_name}} request)

+ Response 201 (application/json)
    OK
    + Attributes({{entity_name}} response)

+ Response 400 (application/json)
    Requisição inválida.
    + Attributes (erro)


## Métodos referentes a uma entidade {{entity_name}} [/{{route}}/{{arguments_in_path[0].name}}/]

+ Parameters
  + {{arguments_in_path[0].name}}: `{{arguments_in_path[0].get_sample()}}` (required, {{arguments_in_path[0].type}}) - {{arguments_in_path[0].get_description()}}.

### Obtém os dados de uma entidade {{entity_name}} [GET]

+ Response 200 (application/json)
    OK
    + Attributes({{entity_name}} response)

+ Response 404 (application/json)
    {{entity_name}} não encontrado.
    + Attributes (erro)

### Atualiza uma entidade {{entity_name}} [PUT]

+ Request Atualiza {{entity_name}} (application/json)
    + Attributes({{entity_name}} request)

+ Response 200 (application/json)
    OK
    + Attributes({{entity_name}} response)

+ Response 400 (application/json)
    Requisição inválida.
    + Attributes (erro)

+ Response 404 (application/json)
    {{entity_name}} não encontrado.
    + Attributes (erro)

### Remove uma entidade {{entity_name}} [DELETE]

+ Response 204 (application/json)

+ Response 404 (application/json)
    {{entity_name}} não encontrado.
    + Attributes (erro)
'''


TPL_OBJECT_DEFINITION = \
u'''## {{entity_name}} request (object)
{% for argument in arguments_in_body %}
- {{argument.name}}: {{argument.get_sample()}} ({{argument.get_type()}}, required) - {{argument.get_description()}}.
{% endfor %}

## {{entity_name}} response (object)
- id_{{arguments_in_path[0].name}}: '123' (number, required) - ID do objeto.
- include {{entity_name}} request
'''


class ApiAryGen(object):
    def __init__(self):
        pass

    def gen(self, parameters):
        template = Template(TPL_ROUTE_DEFINITION)

        print('*** DOC APIARY - Metodos ***\n\n\n' + template.render(parameters))

        template = Template(TPL_OBJECT_DEFINITION)

        print('\n\n\n*** DOC APIARY - Objetos ***\n\n\n' + template.render(parameters))
