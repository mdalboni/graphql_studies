from graphene import InputObjectType
from graphene import String as StringQL, ID
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref

from models.custom_node import CustomNode
from models import Model
from models.pokemon_data import PokemonData


class Pokemon(Model):
    __tablename__ = 'pokemon'
    id = Column('id', Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    data = relationship(
        PokemonData,
        backref=backref('pokemon', cascade='delete,all')
    )

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
        interfaces = (CustomNode,)


class PokemonFields:
    id = ID(source='pk')
    name = StringQL()


class AddPokemonFields(InputObjectType, PokemonFields):
    ...
