# -*- coding: utf-8 -*-

from jinja2 import Template


TPL_URL = \
u'''
from core.views.{{route}} import {{route}}_view, {{route}}_get

...

urlpatterns = [
    ...
    url(r'^{{route}}/$', {{route}}_view),
    url(r'^{{route}}/(?P<{{arguments_in_path[0].name}}>[0-9]+)/$', {{route}}_get),
    ...
'''

TPL_MODEL = \
u'''
class {{entity_name}}(models.Model):
    id_{{arguments_in_path[0].name}} = models.IntegerField(primary_key=True)
    id_estado = models.ForeignKey('Estado', models.DO_NOTHING) # TODO: E quando o nome na tabela nao eh o mesmo?
    id_cidade = models.ForeignKey('Cidade', models.DO_NOTHING)
    id_bairro = models.ForeignKey(Bairro, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = '{{entity_name}}'
'''

TPL_VIEW = \
u'''
# encoding: utf-8
# -*- coding: utf-8 -*-
from core.models import {{entity_name}}
# import core.utils.utils2 as utils
from django.http import JsonResponse
from django.db import transaction, IntegrityError
from core.utils.valida_requisicao_json import check_request
from core.utils.api_errors import ApiError, ApiInvalidRelationship
from rest_framework.decorators import api_view


criar_schema = {
    "type": "object",
    "properties": {
        "nome": {"type": ["string", "null"], "required": True, "minLength": 1},
        "email": {"type": ["string", "null"], "required": True, "minLength": 1},
        "telefone_movel": {
            "type": "object",
            "required": True,
            "properties": {
                "ddd": {"type": ["string", "null"], "minLength": 1, "required": True},
                "numero": {"type": ["string", "null"], "minLength": 1, "required": True}
            }
        },
        "telefone_fixo": {
            "type": "object",
            "required": True,
            "properties": {
                "ddd": {"type": ["string", "null"], "minLength": 1, "required": True},
                "numero": {"type": ["string", "null"], "minLength": 1, "required": True}
            }
        },
        "data_nascimento": {
                            "type": ["string", "null"],
                            "format": "date",
                            "required": True,
                            "minLength": 1
                            },
        "cep": {"type": ["string", "null"], "required": True},
        "endereco_desconhecido": {
                                  "type": ["string", "null"],
                                  "required": True
                                  },
        "numero_logradouro": {"type": ["integer", "null"], "required": True},
        "complemento_logradouro": {
                                   "type": ["string", "null"],
                                   "required": True
                                   },
        "anotacao": {"type": ["string", "null"], "required": True},
        "id_cep": {"type": ["integer", "null"], "required": True},
        "id_estado": {"type": ["integer", "null"], "required": True},
        "id_cidade": {"type": ["integer", "null"], "required": True},
        "id_bairro": {"type": ["integer", "null"], "required": True},
        "perfil_interessado": {
            "type": ["object", "null"],
            "required": True,
            "properties": {
                "id_midia_origem": {"type": ["integer", "null"], "required": True},
                "id_temperatura": {"type": ["integer", "null"], "required": True},
                "id_tipo_nivel_urgencia": {"type": ["integer", "null"], "required": True},
            }
        },
        "perfil_proprietario": {
            "type": ["object", "null"],
            "required": True,
            "properties": {
                "imoveis": {
                            "type": "array", "items": {"type": "integer"},
                            "required": True},
            }
        },
    },
}


def set_{{entity_name}}({{entity_name}}):
    elemento = {}
    elemento['XXX'] = {{entity_name}}.XXX
    ...
    return elemento


# TODO: GET com atomic???
# TODO: Organizar corretamente. Temos GET de todos, POST, GET/PUT/DELETE por ID
@transaction.atomic
@api_view(["GET", "POST", "PUT", "DELETE"])
def {{entity_name}}_view(request, **kwargs):
    # TODO: Valida se os argumentos estao no path
    if 'id_usuario' in kwargs:
        id_usuario = kwargs['id_usuario']
    else:
        return ApiError.invalid_request("Falta parametro id_usuario na url")
        # return ApiError.field_not_found("id_contato")

    # TODO: Se for PUT, GET ou DELETE, o id deve estar no PATH
    if request.method != 'POST':
        if 'id_contato' not in kwargs:
            return ApiError.invalid_request("Falta parametro id_contato na url")

        # TODO: Se for PUT, GET ou DELETE, o objeto deve existir
        id_contato = kwargs['id_contato']
        contatos = Contato.objects.filter(id_contato=id_contato)
        if not contatos:
            return ApiError.resource_not_found('id_contato')
        contato = contatos[0]

    if request.method == 'DELETE':
        # TODO: Coloque seu codigo aqui :-)
        ...
        return JsonResponse({}, safe=False, status=204)

    if request.method == 'GET':
        elemento = set_contato(contato)
        return JsonResponse(elemento, safe=False)
        # else:
        #     usuario = Usuario.objects.filter(id_usuario=id_usuario)
        #     if usuario:
        #         contatos = Contato.objects.filter(usuario=id_usuario)
        #     else:
        #         return ApiError.resource_not_found('id_usuario')

        for contato in contatos:
            elemento = set_contato(contato)
            perfil_interessado = set_perfil_interessado(contato.id_contato)
            if perfil_interessado:
                elemento["perfil_interessado"] = perfil_interessado
            else:
                elemento["perfil_interessado"] = None
            perfil_proprietario = set_perfil_proprietario(contato.id_contato)
            if perfil_proprietario:
                elemento["perfil_proprietario"] = perfil_proprietario
            else:
                elemento["perfil_proprietario"] = None
            resposta.append(elemento)
        resposta = sorted(resposta, key=lambda res: \
                res["exibicao"]["primeira_identificacao"].upper())
        return JsonResponse(resposta, safe=False)

    elif request.method == 'POST' or request.method == 'PUT':
        try:
            with transaction.atomic():
                if request.method == 'POST':
                    data, error = check_request(criar_contatos_schema,
                                                request.body)
                    if error:
                        return error

                if request.method == 'PUT':
                    data, error = check_request(criar_contatos_schema,
                                                request.body,
                                                check_required=False)
                    if error:
                        return error

                    contato = Contato.objects.filter(id_contato=id_contato)
                    if not contato:
                        return ApiError.field_not_found('id_contato')

                    contato = contato[0]
                else:
                    contato = Contato()

                # Se for um PUT nao atualiza o usuario
                if not request.method == 'PUT':
                    # Busca Usuario
                    usuario = Usuario.objects.filter(id_usuario=id_usuario)
                    if usuario:
                        contato.usuario = usuario[0]

                # Valida logica e cria endereco
                if request.method == "PUT":
                    cep, endereco_desconhecido, erro = set_endereco(
                            data, request.method, contato)
                else:
                    cep, endereco_desconhecido, erro = set_endereco(
                            data, request.method)

                if erro:
                    return erro

                if cep:
                    contato.cep_id = cep
                else:
                    contato.cep_id = None

                if endereco_desconhecido:
                    contato.endereco_desconhecido = endereco_desconhecido
                else:
                    contato.endereco_desconhecido = None

                if 'nome' in data:
                    nome = data['nome']
                    if nome:
                        nome, erro = utils.valida_tamanho_campo(
                            data['nome'], 60, 'nome')
                        if erro:
                            return erro
                    contato.nome = nome

                # Validar email
                if 'email' in data:
                    email = data['email']
                    if email:
                        email, erro = utils.valida_tamanho_campo(
                            data['email'], 60, 'email')
                        if erro:
                            return erro

                        email, erro = utils.valida_email(data['email'], 'email')
                        if erro:
                            return erro
                    contato.email = email

                # Validar telefone_movel
                if 'telefone_movel' in data:
                    ddd_telefone_movel, telefone_movel, erro = utils.valida_telefone(data['telefone_movel'], 'telefone_movel')
                    if erro:
                        return erro

                    contato.telefone_movel = telefone_movel
                    contato.ddd_telefone_movel = ddd_telefone_movel

                # Validar telefone_fixo
                if 'telefone_fixo' in data:
                    ddd_telefone_fixo, telefone_fixo, erro = utils.valida_telefone(data['telefone_fixo'], 'telefone_fixo')
                    if erro:
                        return erro

                    contato.telefone_fixo = telefone_fixo
                    contato.ddd_telefone_fixo = ddd_telefone_fixo

                # Validar numero_logradouro
                if 'numero_logradouro' in data:
                    if data['numero_logradouro'] != None:
                        numero, erro = utils.valida_numero_negativo(
                                data['numero_logradouro'], 'numero_logradouro')
                        if numero >= 0:
                            contato.numero_logradouro = numero
                        else:
                            return erro
                    else:
                        contato.numero_logradouro = None

                # Validar data_nascimento
                if 'data_nascimento' in data:
                    data_nascimento = data['data_nascimento']
                    if data_nascimento:
                        data_nascimento, erro = utils.valida_data(
                            data['data_nascimento'], 'data_nascimento')
                        if erro:
                            return erro
                    if not data_nascimento:
                        contato.data_nascimento = data_nascimento
                    else:
                        contato.data_nascimento = utils.formata_data_para_banco(data_nascimento)

                # Validar complemento_logradouro
                if 'complemento_logradouro' in data:
                    if data['complemento_logradouro']:
                        complemento_logradouro, erro = \
                                utils.valida_tamanho_campo(
                            data['complemento_logradouro'], 50,
                            'complemento_logradouro')
                        if complemento_logradouro:
                            contato.complemento_logradouro = \
                                    complemento_logradouro
                        else:
                            return erro
                    else:
                        # TODO: e se complemento_logradouro vier vazio?
                        contato.complemento_logradouro = None

                # Validar anotacao
                if 'anotacao' in data:
                    anotacao = data['anotacao']
                    if anotacao:
                        anotacao, erro = utils.valida_tamanho_campo(
                            data['anotacao'], 400, 'anotacao')
                        if erro:
                            return erro
                    contato.anotacao = anotacao

                if not utils.tem_campos_minimos(contato):
                    return ApiError.invalid_request(
                            "Pelo menos um dos seguintes campos devem "
                            "esta preenchidos: nome, email, telefone_fixo, "
                            "telefone_movel")

                contato.save()

                eh_perfil_proprietario = ('perfil_proprietario' in data) and \
                        data['perfil_proprietario']

                if request.method == 'PUT':
                    perfil_vinculado_interessado = \
                            atualiza_contato_interessado(data, contato)
                    perfil_vinculado_proprietario = \
                            atualiza_contato_proprietario(
                                    eh_perfil_proprietario,
                                    contato)
                    if perfil_vinculado_proprietario:
                        vincula_contato_com_imoveis(
                                contato.id_contato,
                                data['perfil_proprietario']["imoveis"],
                                id_usuario)

                    else:
                        remove_imoveis_de_contato(contato.id_contato)
                else:
                    perfil_vinculado_interessado = \
                        vincula_contato_interessado(data, contato)
                    perfil_vinculado_proprietario = \
                        vincula_contato_proprietario(eh_perfil_proprietario,
                                                     contato)
                    if perfil_vinculado_proprietario:
                        vincula_contato_com_imoveis(
                            contato.id_contato,
                            data['perfil_proprietario']["imoveis"],
                            id_usuario)

                resposta = set_contato(contato)
                if perfil_vinculado_interessado:
                    resposta["perfil_interessado"] = set_perfil_interessado(
                        contato.id_contato)
                else:
                    resposta["perfil_interessado"] = None
                if perfil_vinculado_proprietario:
                    resposta["perfil_proprietario"] = set_perfil_proprietario(
                        contato.id_contato)
                else:
                    resposta["perfil_proprietario"] = None

                if request.method == 'PUT':
                    return JsonResponse(resposta, safe=False, status=200)
                else:
                    return JsonResponse(resposta, safe=False, status=201)

        except IntegrityError as err:
            return ApiError.invalid_request(
               "Inconsistencia nos dados inseridos: %s" % str(err))
        except Exception as err:
            return utils.requisicao_invalida(err)
        except:
            return utils.requisicao_invalida()
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
