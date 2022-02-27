from graphene import InputObjectType
from graphene import String as StringQL, ID
from graphene_sqlalchemy import SQLAlchemyObjectType

from models.custom_node import CustomNode
from models.tables import Pokemon


class PokemonSQL(SQLAlchemyObjectType):
    class Meta:
        model = Pokemon
        interfaces = (CustomNode,)


class PokemonFields:
    id = ID(source='pk')
    name = StringQL()


class AddPokemonFields(InputObjectType, PokemonFields):
    ...
