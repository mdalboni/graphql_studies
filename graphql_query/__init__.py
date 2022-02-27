from graphene import ObjectType, List, String, Schema, Field, Int
from graphene.relay import Node
from graphene_sqlalchemy import SQLAlchemyConnectionField
from models.pokemon import PokemonSQL, Pokemon
from models.pokemon_data import PokemonDataSQL, PokemonData


class PokemonQuery(ObjectType):
    get_pokemons = List(PokemonSQL)
    get_pokemon_by_name = Field(PokemonSQL, name=String())
    get_pokemons_by_name = List(PokemonSQL, name=String())

    list_pokemons = SQLAlchemyConnectionField(
        PokemonSQL.connection,  # noqa
        sort=None
    )

    @staticmethod
    def resolve_pokemon_by_name(parent, info, **kwargs):  # noqa
        name = kwargs.get('name')
        query = PokemonSQL.get_query(info)
        return query.filter(Pokemon.name == name).first()

    @staticmethod
    def resolve_get_pokemons(parent, info, **kwargs):
        return PokemonSQL.get_query(info).all()

    @staticmethod
    def resolve_pokemons_by_name(parent, info, **kwargs):
        name = kwargs.get('name')
        query = PokemonSQL.get_query(info)
        return query.filter(Pokemon.name.contains(name)).all()


class PokemonDataQuery(ObjectType):
    get_pokemon_data = Field(PokemonDataSQL, id=Int())

    @staticmethod
    def resolve_get_pokemon_data(parent, info, **kwargs):
        id = kwargs.get('id')
        query = PokemonDataSQL.get_query(info)
        return query.filter(PokemonData.id == id).first()


class Query(PokemonQuery, PokemonDataQuery):
    node = Node.Field()


schema = Schema(
    query=Query, mutation=None, types=[PokemonSQL, PokemonDataSQL]
)
introspection_dict = schema.introspect()
