from graphene import ObjectType, List, String, Schema, Field
# from graphene.relay import Node
# from graphene_sqlalchemy import SQLAlchemyConnectionField

from models import Pokemon
from models.pokemon import PokemonSQL


class PokemonQuery(ObjectType):
    get_pokemons = List(PokemonSQL)
    pokemon_by_name = List(PokemonSQL, name=String())

    # all_pokemon = SQLAlchemyConnectionField(PokemonSQL.connection)

    @staticmethod
    def resolve_get_pokemons(parent, info, **kwargs):
        return PokemonSQL.get_query(info).all()

    @staticmethod
    def resolve_pokemon_by_name(parent, info, **kwargs):
        name = kwargs.get('name')
        query = PokemonSQL.get_query(info)
        return query.filter(Pokemon.name.contains(name)).all()


class PokemonQuery2(ObjectType):
    get_pokemon_name = Field(PokemonSQL, name=String())

    @staticmethod
    def resolve_get_pokemon_name(parent, info, **kwargs):
        name = kwargs.get('name')
        query = PokemonSQL.get_query(info)
        return query.filter(Pokemon.name == name).first()


class Query(PokemonQuery, PokemonQuery2):
    ...


schema = Schema(
    query=Query, mutation=None, types=[PokemonSQL]
)
