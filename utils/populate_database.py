from security.safe_requests import get
from sqlalchemy.orm import sessionmaker

from models import engine, Pokemon, PokemonData

Session = sessionmaker(bind=engine)
POKEMON_URL = 'https://pokeapi.co/api/v2/pokemon/?offset=0&limit={}'
POKEMON_DATA_URL = 'https://pokeapi.co/api/v2/pokemon/{}/'
session = Session()

pokemon_not_found = 'https://pm1.narvii.com/6715/bc85ac4e3704c7cdd9e3d5e556d25a5ade9c5f13_hq.jpg'


def get_and_save_pokemon(limit=151):
    response = get(POKEMON_URL.format(limit))
    if response.status_code != 200:
        raise Exception
    pokemons = response.json()['results']
    for pokemon in pokemons:
        poke = Pokemon(**pokemon)
        session.add(poke)
        session.commit()
        print(f'Salvando o pokemon: {poke.id}')
        get_and_save_pokemon_data(poke.id)


def get_and_save_pokemon_data(id):
    response = get(POKEMON_DATA_URL.format(id))
    if response.status_code != 200:
        raise Exception
    data = response.json()
    data['pokemon_id'] = data.get('id')
    data['sprite'] = (
        data.get('sprites', {})
            .get('other', {})
            .get('official-artwork', {})
            .get('front_default', pokemon_not_found)
    )
    session.add(PokemonData(**data))
    session.commit()


if __name__ == "__main__":
    get_and_save_pokemon()
    session.close()
