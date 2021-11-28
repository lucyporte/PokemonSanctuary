from random import choice


class Background():
    """
    Manage background images
    """

    def __init__(self, name, image, pokemonSpawns, disallowedRegions, dangerRegions):
        self._name = name
        self._image = image
        self._pokemonSpawns = pokemonSpawns
        self._left = None
        self._right = None
        self._beneath = None
        self._above = None
        self._disallowedRegions = disallowedRegions
        self._dangerRegions = dangerRegions

    def getName(self):
        """
        Get zone name
        """
        return self._name

    def getImage(self):
        """
        Get file path to image PNG
        """
        return self._image

    def getAllPokemonSpawns(self):
        """
        Get all coordinates deemed suitable for Pokemon spawns
        """
        return self._pokemonSpawns

    def getRandomPokemonSpawn(self):
        """
        Get a random set of coordinates deemed suitable for Pokemon spawns
        """
        return choice(self.getAllPokemonSpawns())

    def setLeft(self, left):
        """
        Set the zone which should appear when a player exits this zone to the left
        """
        self._left = left

    def getLeft(self):
        """
        Get the zone which will appear when a player exits this zone to the left

        Returns None if no zone is set
        """
        return self._left

    def setRight(self, right):
        """
        Set the zone which should appear when a player exits this zone to the right
        """
        self._right = right

    def getRight(self):
        """
        Get the zone which will appear when a player exits this zone to the right

        Returns None if no zone is set
        """
        return self._right

    def setBeneath(self, beneath):
        """
        Set the zone which should appear when a player exits this zone at the bottom
        """
        self._beneath = beneath

    def getBeneath(self):
        """
        Get the zone which will appear when a player exits this zone at the bottom

        Returns None if no zone is set
        """
        return self._beneath

    def setAbove(self, above):
        """
        Set the zone which should appear when a player exits this zone at the top
        """
        self._above = above

    def getAbove(self):
        """
        Get the zone which will appear when a player exits this zone at the top

        Returns None if no zone is set
        """
        return self._above

    def isDisallowedRegion(self, x, y):
        """
        Checks if a player has entered a disallowed region of this zone

        Returns True if the player is in a disallowed region. Otherwise, returns False.
        """
        for region in self._disallowedRegions:
            if region[0] < x < region[2] and region[1] < y < region[3]:
                return True
        return False

    def isDangerRegion(self, x, y):
        """
        Checks if a player has entered a dangerous region of this zone

        Returns True if the player is in a dangerous region. Otherwise, returns False.
        """
        for region in self._dangerRegions:
            if region[0] < x < region[2] and region[1] < y < region[3]:
                return True
        return False


def getMaps():
    """
    Returns all zones which make up the map
    """
    return [forest, spawn, city, meadow, canyon]


def getFirstMap():
    """
    Returns the spawn zone
    """
    return spawn


# Initialise all zones
forest = Background(
    "Forest",
    "assets/images/maps/forest.png",
    [
        [195, 155]
    ],
    [
        [120, 175, 190, 225],
        [210, 175, 280, 225],
        [120, 85, 185, 135],
        [210, 85, 275, 135],
        [125, 260, 400, 400],
        [0, 0, 90, 230],
        [0, 260, 90, 400],
        [305, 0, 400, 230],
        [90, 0, 260, 50]
    ],
    []
)
spawn = Background(
    "Spawn",
    "assets/images/maps/spawn.png",
    [
        [155, 205],
        [155, 290],
        [245, 290],
        [245, 205]
    ],
    [
        [160, 40, 240, 115],
        [190, 220, 225, 250]
    ],
    []
)
city = Background(
    "City",
    "assets/images/maps/city.png",
    [
        [160, 110]
    ],
    [
        [25, 40, 85, 120],
        [85, 5, 150, 120],
        [0, 185, 185, 235],
        [0, 260, 185, 400],
        [225, 195, 280, 400],
        [225, 0, 400, 165],
        [310, 315, 365, 365]
    ],
    []
)
meadow = Background(
    "Meadow",
    "assets/images/maps/meadow.png",
    [
        [95, 255]
    ],
    [],
    [
        [0, 325, 40, 380],
        [40, 335, 100, 390],
        [100, 325, 120, 380],
        [120, 315, 175, 370],
        [160, 310, 215, 360],
        [190, 295, 235, 335],
        [195, 280, 250, 310],
        [195, 200, 250, 230],
        [185, 160, 240, 200],
        [180, 125, 235, 160],
        [190, 85, 245, 125],
        [200, 50, 250, 85],
        [205, 15, 260, 50],
        [215, 0, 270, 15]
    ]
)
canyon = Background(
    "Canyon",
    "assets/images/maps/canyon.png",
    [
        [190, 220]
    ],
    [],
    [
        [250, 0, 355, 35],
        [245, 35, 350, 70],
        [240, 70, 345, 110],
        [245, 105, 350, 140],
        [240, 145, 345, 175],
        [235, 180, 340, 215],
        [230, 220, 335, 220],
        [230, 275, 340, 300],
        [235, 300, 345, 335],
        [240, 335, 350, 370],
        [245, 370, 355, 390],
        [250, 400, 360, 400]
    ]
)

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
