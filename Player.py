"""
Aqui você vai inserir as informações do jogador que serão tratadas ao movimentar
ele, como vida, stamina/energia, etc
"""

class Player:
    # Inicializa o jogador
    def __init__(self, name, life, stamina):
        self.__life = life
        self.__name = name
        self.__stamina = stamina
        self.__position = 1

    # Retorna o nome do jogador
    def getName(self):
        return self.name
    
    # Dar dano no jogador
    #TODO: Precisa verificar se o jogador morre
    def takeDamage(self, dano):
        self.__currentLife -= dano
    
    # Retorna a vida atual
    def getLife(self):
        return self.__currentLife
    
    def resetLife(self):
        self.__currentLife = self.__life
    
    def resetStamina(self):
        self.__currentStamina = self.stamina
    
    # decrementar a stamina
    def lossStamina(self, cost):
        self.__currentStamina -= cost
    
    # Retorna a stamina atual
    def getStamina(self):
        return self.__currentStamina
    
    # Altera posição do jogador
    def setPosition(self, new_position):
        self.__position = new_position

    # Retorna a posição atual do jogador
    def getPosition(self):
        return self.__position



        