class Player:
    def __init__(self, name, sprint, dribble, passing, shooting):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    # @name.setter
    # def name(self, value):
    #     self.__name = value

    def __str__(self):
        return (f"Player: {self.__name}\nSprint: {self.__sprint}\nDribble: "
                f"{self.__dribble}\nPassing: {self.__passing}\nShooting: {self.__shooting}")

