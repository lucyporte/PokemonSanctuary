from random import choice




class Pokemon():
    """
    Manage Pokemon data
    """

    def __init__(self, id, name, left, right, up, down):
        self._id = id
        self._name = name
        self._left = left
        self._right = right
        self._up = up
        self._down = down

    def get_id(self):
        """
        Get Pokemon internal ID
        """
        return self._id

    def get_name(self):
        """
        Get name of the Pokemon
        """
        return self._name

    def get_left_walk_sprite(self):
        """
        Get the sprites of this Pokemon when it faces to the left
        """
        return self._left

    def get_right_walk_sprite(self):
        """
        Get the sprites of this Pokemon when it faces to the right
        """
        return self._right

    def get_up_walk_sprite(self):
        """
        Get the sprites of this Pokemon when it faces away from the viewer
        """
        return self._up

    def get_down_walk_sprite(self):
        """
        Get the sprites of this Pokemon when it faces towards from the viewer
        """
        return self._down


class PokemonWalkingAnimation():
    """
    Manage collections of Pokemon sprites which form an animation
    """
    def __init__(self, frame1, frame2):
        self._frame1 = frame1
        self._frame2 = frame2

    def get_frame_1(self):
        """
        Get the first frame in the animation
        """
        return self._frame1

    def get_frame_2(self):
        """
        Get the second frame in the animation
        """
        return self._frame2


class PokemonImage():
    """
    Manage a Pokemon sprite
    """
    def __init__(self, path, width, height):
        self._path = path
        self._width = width
        self._height = height

    def get_path(self):
        """
        Get file path to image PNG
        """
        return self._path

    def get_width(self):
        """
        Get width of the image in pixels
        """
        return self._width

    def get_height(self):
        """
        Get height of the image in pixels
        """
        return self._height


class PokemonManager():
    def __init__(self):
        self._pokemon = []
        self._available_pokemon = []
        self._saved_pokemon = []
        self.initialise_all_pokemon()

    def add_pokemon(self, pokemon):
        self._pokemon += pokemon
        self._available_pokemon += pokemon

    def get_all_pokemon(self):
        return self._pokemon

    def get_all_available_pokemon(self):
        return self._available_pokemon

    def get_random_available_pokemon(self):
        if len(self._available_pokemon) == 0:
            return None
        return choice(self.get_all_available_pokemon())

    def save_pokemon(self, pokemon):
        self._available_pokemon.remove(pokemon.data)
        self._saved_pokemon.append(pokemon.data)

    def initialise_all_pokemon(self):
        pokemon1 = Pokemon(
            "1",
            "Chesspin",
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/1/left1.png",
                    18,
                    18
                ),
                PokemonImage(
                    "assets/images/pokemon/1/left2.png",
                    18,
                    18
                )
            ),
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/1/right1.png",
                    18,
                    18
                ),
                PokemonImage(
                    "assets/images/pokemon/1/right2.png",
                    18,
                    18
                )
            ),
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/1/away1.png",
                    21,
                    19
                ),
                PokemonImage(
                    "assets/images/pokemon/1/away2.png",
                    21,
                    19
                )
            ),
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/1/towards1.png",
                    21,
                    19
                ),
                PokemonImage(
                    "assets/images/pokemon/1/towards2.png",
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
                    "assets/images/pokemon/2/left1.png",
                    23,
                    23
                ),
                PokemonImage(
                    "assets/images/pokemon/2/left2.png",
                    26,
                    22
                )
            ),
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/2/right1.png",
                    26,
                    23
                ),
                PokemonImage(
                    "assets/images/pokemon/2/right2.png",
                    26,
                    22
                )
            ),
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/2/away1.png",
                    28,
                    22
                ),
                PokemonImage(
                    "assets/images/pokemon/2/away2.png",
                    26,
                    23
                )
            ),
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/2/towards1.png",
                    26,
                    23
                ),
                PokemonImage(
                    "assets/images/pokemon/2/towards2.png",
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
                    "assets/images/pokemon/3/left1.png",
                    32,
                    32
                ),
                PokemonImage(
                    "assets/images/pokemon/3/left2.png",
                    32,
                    32
                )
            ),
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/3/right1.png",
                    32,
                    32
                ),
                PokemonImage(
                    "assets/images/pokemon/3/right2.png",
                    32,
                    32
                )
            ),
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/3/away1.png",
                    32,
                    32
                ),
                PokemonImage(
                    "assets/images/pokemon/3/away2.png",
                    32,
                    32
                )
            ),
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/3/towards1.png",
                    32,
                    32
                ),
                PokemonImage(
                    "assets/images/pokemon/3/towards2.png",
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
                    "assets/images/pokemon/4/left1.png",
                    32,
                    32
                ),
                PokemonImage(
                    "assets/images/pokemon/4/left2.png",
                    32,
                    32
                )
            ),
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/4/right1.png",
                    32,
                    32
                ),
                PokemonImage(
                    "assets/images/pokemon/4/right2.png",
                    32,
                    32
                )
            ),
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/4/away1.png",
                    32,
                    32
                ),
                PokemonImage(
                    "assets/images/pokemon/4/away2.png",
                    32,
                    32
                )
            ),
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/4/towards1.png",
                    32,
                    32
                ),
                PokemonImage(
                    "assets/images/pokemon/4/towards2.png",
                    32,
                    32
                )
            )
        )

        pokemon5 = Pokemon(
            "5",
            "Pokemon 5",
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/5/left1.png",
                    16,
                    21
                ),
                PokemonImage(
                    "assets/images/pokemon/5/left2.png",
                    16,
                    21
                )
            ),
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/5/right1.png",
                    16,
                    21
                ),
                PokemonImage(
                    "assets/images/pokemon/5/right2.png",
                    16,
                    21
                )
            ),
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/5/away1.png",
                    21,
                    21
                ),
                PokemonImage(
                    "assets/images/pokemon/5/away2.png",
                    21,
                    21
                )
            ),
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/5/towards1.png",
                    21,
                    21
                ),
                PokemonImage(
                    "assets/images/pokemon/5/towards2.png",
                    32,
                    21
                )
            )
        )

        pokemon6 = Pokemon(
            "6",
            "Pokemon 6",
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/6/left1.png",
                    25,
                    22
                ),
                PokemonImage(
                    "assets/images/pokemon/6/left2.png",
                    26,
                    22
                )
            ),
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/6/right1.png",
                    25,
                    22
                ),
                PokemonImage(
                    "assets/images/pokemon/6/right2.png",
                    26,
                    22
                )
            ),
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/6/away1.png",
                    15,
                    25
                ),
                PokemonImage(
                    "assets/images/pokemon/6/away2.png",
                    15,
                    25
                )
            ),
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/6/towards1.png",
                    15,
                    23
                ),
                PokemonImage(
                    "assets/images/pokemon/6/towards2.png",
                    15,
                    23
                )
            )
        )

        pokemon7 = Pokemon(
            "7",
            "Pokemon 7",
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/7/left1.png",
                    28,
                    26
                ),
                PokemonImage(
                    "assets/images/pokemon/7/left2.png",
                    26,
                    26
                )
            ),
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/7/right1.png",
                    24,
                    26
                ),
                PokemonImage(
                    "assets/images/pokemon/7/right2.png",
                    23,
                    26
                )
            ),
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/7/away1.png",
                    28,
                    26
                ),
                PokemonImage(
                    "assets/images/pokemon/7/away2.png",
                    26,
                    26
                )
            ),
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/7/towards1.png",
                    28,
                    26
                ),
                PokemonImage(
                    "assets/images/pokemon/7/towards2.png",
                    26,
                    26
                )
            )
        )

        pokemon8 = Pokemon(
            "8",
            "Pokemon 8",
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/8/left1.png",
                    18,
                    18
                ),
                PokemonImage(
                    "assets/images/pokemon/8/left2.png",
                    12,
                    21
                )
            ),
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/8/right1.png",
                    18,
                    18
                ),
                PokemonImage(
                    "assets/images/pokemon/8/right2.png",
                    12,
                    21
                )
            ),
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/8/away1.png",
                    23,
                    18
                ),
                PokemonImage(
                    "assets/images/pokemon/8/away2.png",
                    17,
                    20
                )
            ),
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/8/towards1.png",
                    23,
                    18
                ),
                PokemonImage(
                    "assets/images/pokemon/8/towards2.png",
                    17,
                    20
                )
            )
        )

        pokemon9 = Pokemon(
            "9",
            "Pokemon 9",
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/9/left1.png",
                    25,
                    24
                ),
                PokemonImage(
                    "assets/images/pokemon/9/left2.png",
                    25,
                    24
                )
            ),
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/9/right1.png",
                    25,
                    24
                ),
                PokemonImage(
                    "assets/images/pokemon/9/right2.png",
                    25,
                    24
                )
            ),
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/9/away1.png",
                    25,
                    24
                ),
                PokemonImage(
                    "assets/images/pokemon/9/away2.png",
                    25,
                    24
                )
            ),
            PokemonWalkingAnimation(
                PokemonImage(
                    "assets/images/pokemon/9/towards1.png",
                    25,
                    24
                ),
                PokemonImage(
                    "assets/images/pokemon/9/towards2.png",
                    25,
                    24
                )
            )
        )

        self.add_pokemon([
            pokemon1,
            pokemon2,
            pokemon3,
            pokemon4,
            pokemon5,
            pokemon6,
            pokemon7,
            pokemon8,
            pokemon9
        ])
