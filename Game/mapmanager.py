from random import choice

class Background():
    def __init__(self, name, image, pokemonSpawns):
        self._name = name
        self._image = image
        self._pokemonSpawns = pokemonSpawns
        self._left = None
        self._right = None
        self._beneath = None
        self._above = None

    def getName(self):
        return self._name

    def getImage(self):
        return self._image

    def getAllPokemonSpawns(self):
        return self._pokemonSpawns

    def getRandomPokemonSpawn(self):
        return choice(self.getAllPokemonSpawns())

    def setLeft(self, left):
        self._left = left

    def getLeft(self):
        return self._left
    
    def setRight(self, right):
        self._right = right

    def getRight(self):
        return self._right

    def setBeneath(self, beneath):
        self._beneath = beneath

    def getBeneath(self):
        return self._beneath

    def setAbove(self, above):
        self._above = above

    def getAbove(self):
        return self._above

def getMaps():
    return [forest, spawn, city, meadow, canyon]

def getFirstMap():
    return spawn

forest = Background("Forest", "assets/maps/forest.png", [[195, 155]])
spawn = Background("Spawn", "assets/maps/spawn.png", [[155, 205], [155, 290], [245, 290], [245, 205]])
city = Background("City", "assets/maps/city.png", [[160, 110]])
meadow = Background("Meadow", "assets/maps/meadow.png", [[95, 255]])
canyon = Background("Canyon", "assets/maps/canyon.png", [[190, 220]])

forest.setRight(spawn)
forest.setBeneath(meadow)

spawn.setLeft(forest)
spawn.setBeneath(canyon)
spawn.setRight(city)

city.setLeft(spawn)

meadow.setAbove(forest)
meadow.setRight(canyon)

canyon.setLeft(meadow)
canyon.setAbove(spawn)