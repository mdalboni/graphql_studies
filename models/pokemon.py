from graphene import String as StringQL, InputObjectType, ID
from graphene.relay import Node
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import Column, Integer, String

from models import Model


class Pokemon(Model):
    __tablename__ = 'pokemon'
    id = Column('id', Integer, primary_key=True)
    name = Column(String(200))

    def __init__(self, name, id=None, *args, **kwargs):
        self.name = name
        self.id = id

    def to_json(self):
        return dict(name=self.name)

    def __eq__(self, other):
        return type(self) is type(other) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)


class PokemonSQL(SQLAlchemyObjectType):
    class Meta:
        model = Pokemon
        # interfaces = (Node,)


class PokemonFields:
    id = ID(source='pk')
    name = StringQL()


class AddPokemonFields(InputObjectType, PokemonFields):
    ...
