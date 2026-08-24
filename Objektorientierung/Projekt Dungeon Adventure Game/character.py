class Character:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def getName(self):
        return self.__name

    def setName(self, name : str):
         self.__name = name

c = Character("Aragorn", 150)

print(c.getName())

c.setName("Legolas")

print(c.getName())