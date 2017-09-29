# -*- coding: utf-8 -*-

from jinja2 import Template


TPL_URL = \
u'''
from core.views.{{route}} import {{route}}_view, {{route}}_get

...

urlpatterns = [
    ...
    url(r'^{{route}}/$', {{route}}_view),
    url(r'^{{route}}/(?P<{{key_name}}>[0-9]+)/$', {{route}}_get),
    ...
'''

TPL_MODEL = \
u'''
class {{entity_name}}(models.Model):
    {{key_name}} = models.IntegerField(primary_key=True)
    id_estado = models.ForeignKey('Estado', models.DO_NOTHING) # TODO: E quando o nome na tabela nao eh o mesmo?
    id_cidade = models.ForeignKey('Cidade', models.DO_NOTHING)
    id_bairro = models.ForeignKey(Bairro, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = '{{entity_name}}'
'''


class DjangoRestApiGen(object):
    def __init__(self):
        pass

    def gen(self, parameters):
        self.__gen_route(parameters)
        self.__gen_model(parameters)
        # e1.gen_view()

    def __gen_route(self, parameters):
        template = Template(TPL_URL)

        print('\n\n\n*** URL.PY ***\n\n\n' + template.render(parameters))


    def __gen_model(self, parameters):
        template = Template(TPL_MODEL)

        print('\n\n\n*** MODELS.PY ***\n\n\n' + template.render(parameters))
