import json

import PokemonManager


def read():
    """
    Read data from the database.
    """
    file = open("data/pokemon.json")
    data = json.load(file)
    file.close()
    return data


def write(data):
    """
    Write data to the database.
    """
    file = open("data/pokemon.json", "w")
    data = json.dump(data, file)
    file.close()


def update(id, difference):
    """
    Update statistics for a particular Pokemon.
    """
    data = read()
    if id in data.keys():
        data[id] += difference
        write(data)


def prepare():
    """
    Adds any missing Pokemon IDs into our database.
    """
    data = read()
    keys = data.keys()
    for pokemon in PokemonManager.get_all():
        id = pokemon.get_id()
        if id not in keys:
            data[id] = 0
    write(data)
