class Player:
    def __init__(self, name, life, stamina):
        self.__life = life
        self.__name = name
        self.__stamina = stamina
        self.__position = 1

    def getName(self):
        return self.name
    
    def takeDamage(self, dano):
        self.__life -= dano
    
    def getLife(self):
        return self.__life
    
    def lossStamina(self, cost):
        self.__stamina -= cost
    
    def getStamina(self):
        return self.__stamina
    
    def setPosition(self, new_position):
        self.__position = new_position

    def getPosition(self):
        return self.__position



        