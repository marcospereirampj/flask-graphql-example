import requests
from graphene import ObjectType, String, ID, List, Int

import json

from collections import namedtuple

API_URL_DEPUTY = "https://dadosabertos.camara.leg.br/api/v2/deputados"


def _json_object_hook(d):
    return namedtuple('X', d.keys())(*d.values())


def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)


class Deputy(ObjectType):
    id = ID()
    uri = String()
    nome = String()
    sigla_partido = String()
    uri_partido = String()
    sigla_uf = String()
    id_legislatura = Int()
    url_foto = String()


class Query(ObjectType):
    deputies = List(Deputy, per_page=Int(required=False), page=Int(required=False))

    def resolve_deputies(self, info, per_page=20, page=1):
        response = requests.get(API_URL_DEPUTY,
                                headers={'Content-Type': 'application/json'},
                                params={'itens': per_page, 'pagina': page})
        return json2obj(json.dumps(response.json()['dados']))
