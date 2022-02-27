from graphene import String as StringQL, Int, ID
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String

from models import Model


class PokemonData(Model):
    __tablename__ = 'pokemon_data'
    id = Column('id', Integer, primary_key=True)
    pokemon_id = Column(Integer, ForeignKey('pokemon.id'))
    height = Column(Integer())
    is_default = Column(Boolean())
    order = Column(Integer())
    weight = Column(Integer())
    sprite = Column(String(200))

    def __init__(
            self, id, pokemon_id, height, is_default, order, weight,
            sprite, *args, **kwargs
    ):
        self.id = id
        self.pokemon_id = pokemon_id
        self.height = height
        self.is_default = is_default
        self.order = order
        self.weight = weight
        self.sprite = sprite

    def to_json(self):
        return dict(
            id=self.id,
            pokemon_id=self.pokemon_id,
            height=self.height,
            is_default=self.is_default,
            order=self.order,
            weight=self.weight,
            sprite=self.sprite
        )

    def __eq__(self, other):
        return type(self) is type(other) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)


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
