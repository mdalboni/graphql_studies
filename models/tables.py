from sqlalchemy import Column, Integer, Boolean, ForeignKey, String
from sqlalchemy.orm import relationship

from models import Model


class Pokemon(Model):
    __tablename__ = 'pokemon'
    id = Column('id', Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    data = relationship(
        "PokemonData",
        back_populates="parent",
        uselist=False
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


class PokemonData(Model):
    __tablename__ = 'pokemon_data'
    id = Column('id', Integer, primary_key=True)
    pokemon_id = Column(Integer, ForeignKey('pokemon.id'), nullable=False)
    height = Column(Integer(), nullable=False)
    is_default = Column(Boolean(), nullable=False)
    order = Column(Integer(), nullable=False)
    weight = Column(Integer(), nullable=False)
    sprite = Column(String(200), nullable=False)
    parent = relationship(
        Pokemon, back_populates="data"
    )

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
