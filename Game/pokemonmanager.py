from random import choice

class Pokemon():
    def __init__(self, id, name, left, right, up, down):
        self._id = id
        self._name = name
        self._left = left
        self._right = right
        self._up = up
        self._down = down

    def getID(self):
        return self._id

    def getName(self):
        return self._name

    def getLeftWalkSprite(self):
        return self._left

    def getRightWalkSprite(self):
        return self._right

    def getUpWalkSprite(self):
        return self._up

    def getDownWalkSprite(self):
        return self._down

class PokemonWalkingAnimation():
    def __init__(self, frame1, frame2):
        self._frame1 = frame1
        self._frame2 = frame2

    def getFrame1(self):
        return self._frame1

    def getFrame2(self):
        return self._frame2

class PokemonImage():
    def __init__(self, path, width, height):
        self._path = path
        self._width = width
        self._height = height

    def getPath(self):
        return self._path

    def getWidth(self):
        return self._width

    def getHeight(self):
        return self._height

def getAll():
    return [pokemon1, pokemon2, pokemon3, pokemon4]

def getRandom():
    return choice(getAll())

pokemon1 = Pokemon(
    "1",
    "Chesspin",
    PokemonWalkingAnimation(
        PokemonImage(
            "assets/pokemon/1/left1.png",
            18,
            18
        ),
        PokemonImage(
            "assets/pokemon/1/left2.png",
            18,
            18
        )
    ),
    PokemonWalkingAnimation(
        PokemonImage(
            "assets/pokemon/1/right1.png",
            18,
            18
        ),
        PokemonImage(
            "assets/pokemon/1/right2.png",
            18,
            18
        )
    ),
    PokemonWalkingAnimation(
        PokemonImage(
            "assets/pokemon/1/away1.png",
            21,
            19
        ),
        PokemonImage(
            "assets/pokemon/1/away2.png",
            21,
            19
        )
    ),
    PokemonWalkingAnimation(
        PokemonImage(
            "assets/pokemon/1/towards1.png",
            21,
            19
        ),
        PokemonImage(
            "assets/pokemon/1/towards2.png",
            21,
            19
        )
    )
)

pokemon2 = Pokemon(
    "2",
    "Butterfly",
    PokemonWalkingAnimation(
        PokemonImage(
            "assets/pokemon/2/left1.png",
            23,
            23
        ),
        PokemonImage(
            "assets/pokemon/2/left2.png",
            26,
            22
        )
    ),
    PokemonWalkingAnimation(
        PokemonImage(
            "assets/pokemon/2/right1.png",
            26,
            23
        ),
        PokemonImage(
            "assets/pokemon/2/right2.png",
            26,
            22
        )
    ),
    PokemonWalkingAnimation(
        PokemonImage(
            "assets/pokemon/2/away1.png",
            28,
            22
        ),
        PokemonImage(
            "assets/pokemon/2/away2.png",
            26,
            23
        )
    ),
    PokemonWalkingAnimation(
        PokemonImage(
            "assets/pokemon/2/towards1.png",
            26,
            23
        ),
        PokemonImage(
            "assets/pokemon/2/towards2.png",
            28,
            22
        )
    )
)

pokemon3 = Pokemon(
    "3",
    "Comrade Dragon",
    PokemonWalkingAnimation(
        PokemonImage(
            "assets/pokemon/3/left1.png",
            32,
            32
        ),
        PokemonImage(
            "assets/pokemon/3/left2.png",
            32,
            32
        )
    ),
    PokemonWalkingAnimation(
        PokemonImage(
            "assets/pokemon/3/right1.png",
            32,
            32
        ),
        PokemonImage(
            "assets/pokemon/3/right2.png",
            32,
            32
        )
    ),
    PokemonWalkingAnimation(
        PokemonImage(
            "assets/pokemon/3/away1.png",
            32,
            32
        ),
        PokemonImage(
            "assets/pokemon/3/away2.png",
            32,
            32
        )
    ),
    PokemonWalkingAnimation(
        PokemonImage(
            "assets/pokemon/3/towards1.png",
            32,
            32
        ),
        PokemonImage(
            "assets/pokemon/3/towards2.png",
            32,
            32
        )
    )
)

pokemon4 = Pokemon(
    "4",
    "Miss Comrade",
    PokemonWalkingAnimation(
        PokemonImage(
            "assets/pokemon/4/left1.png",
            32,
            32
        ),
        PokemonImage(
            "assets/pokemon/4/left2.png",
            32,
            32
        )
    ),
    PokemonWalkingAnimation(
        PokemonImage(
            "assets/pokemon/4/right1.png",
            32,
            32
        ),
        PokemonImage(
            "assets/pokemon/4/right2.png",
            32,
            32
        )
    ),
    PokemonWalkingAnimation(
        PokemonImage(
            "assets/pokemon/4/away1.png",
            32,
            32
        ),
        PokemonImage(
            "assets/pokemon/4/away2.png",
            32,
            32
        )
    ),
    PokemonWalkingAnimation(
        PokemonImage(
            "assets/pokemon/4/towards1.png",
            32,
            32
        ),
        PokemonImage(
            "assets/pokemon/4/towards2.png",
            32,
            32
        )
    )
)