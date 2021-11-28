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


def analyse(id):
    """
    Analyse how dangerous a Pokemon is
    """
    data = read()
    if id in data.keys() and data[id] != 0:
        if data[id] > (sum(data.values()) / len(data.values())):
            return ["You sense a Pokemon here.", "It has a lot of power.", "You are not yet ready."]
        return ["You sense a Pokemon here.", "You can outmatch it easily.", "You should take on the battle."]
    return ["You sense a Pokemon here.", "The odds are promising.", "You should take on the battle."]


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
