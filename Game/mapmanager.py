class Background():
    def __init__(self, name, image):
        self._name = name
        self._image = image
        self._left = None
        self._right = None
        self._beneath = None
        self._above = None

    def getName(self):
        return self._name

    def getImage(self):
        return self._image

    def setLeft(self, left):
        self._left = left

    def getLeft(self):
        return self.left
    
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

forest = Background("Forest", "assets/forest.png")
spawn = Background("Spawn", "assets/spawn.png")
city = Background("City", "assets/city.png")
meadow = Background("Meadow", "assets/meadow.png")
canyon = Background("Canyon", "assets/canyon.png")

forest.setRight(spawn)
forest.setBeneath(meadow)

spawn.setLeft(forest)
spawn.setBeneath(canyon)
spawn.setRight(city)

city.setLeft(spawn)

meadow.setAbove(forest)
meadow.setRight(canyon)

canyon.setLeft(meadow)
meadow.setAbove(spawn)