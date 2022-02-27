from graphene import String as StringQL, Int, ID
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import Boolean

from models.tables import PokemonData


class PokemonDataSQL(SQLAlchemyObjectType):
    class Meta:
        model = PokemonData
        # interfaces = (Node,)


class PokemonDataFields:
    name = StringQL()
    id = ID(source='pk')
    pokemon_id = ID(source='fk')
    height = Int()
    is_default = Boolean()
    order = Int()
    weight = Int()
    sprite = StringQL()
