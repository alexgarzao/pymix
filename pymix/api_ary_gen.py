# -*- coding: utf-8 -*-

from jinja2 import Template


TPL_ROUTE_DEFINITION = \
u'''## Rotas para criar/listar a entidade {{entity_name}} [/{{route}}/]

### Lista todas as entidades {{entity_name}} [GET]

+ Response 200 (application/json)
    + Attributes(array[{{entity_name}} response])

### Cria uma nova entidade {{entity_name}} [POST]

+ Request Cria {{entity_name}} (application/json)
    + Attributes({{entity_name}} response)

+ Response 201 (application/json)
    OK
    + Attributes({{entity_name}} response)

+ Response 400 (application/json)
    Requisição inválida.
    + Attributes (erro)


## Métodos referentes a uma entidade {{entity_name}} [/{{route}}/{{key_name}}/]

+ Parameters
  + {{key_name}}: `{{key_sample}}` (required, {{key_type}}) - {{key_description}}.

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
- {{property_name}}: {{property_sample}} ({{property_type}}, required) - {{property_description}}.

## {{entity_name}} response (object)
- id_{{key_name}}: {{key_sample}} ({{key_type}}, required) - {{key_description}}.
- include {{entity_name}} request
'''


class ApiAryGen(object):
    def __init__(self):
        pass

    def gen(self, parameters):
        template = Template(TPL_ROUTE_DEFINITION)

        print('*** DOC APIARY ***\n\n\n' + template.render(parameters))
