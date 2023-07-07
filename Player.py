# Aqui são inseridas as informações do jogador que serão tratadas ao movimentá-lo, como vida e stamina.

class Player:
    # Inicializa o jogador
    def __init__(self, name, life, stamina):
        self.__name = name
        self.__life = life
        self.__stamina = stamina
        self.__currentLife = self.__life
        self.__currentStamina = self.__stamina
        self.__position = 1
        self.__key = 0

    # Retorna o nome do jogador
    def getName(self):
        return self.name
    
    # Retorna a vida atual
    def getLife(self):
        return self.__currentLife
    
    # Atribui dano ao jogador
    def takeDamage(self, damage):
        self.__currentLife -= damage
    
    # Recupera totalmente a vida
    def resetLife(self):
        self.__currentLife = self.__life
    
    # Retorna a stamina atual
    def getStamina(self):
        return self.__currentStamina
    
    # Decrementa a stamina
    def lossStamina(self, cost):
        self.__currentStamina -= cost

    # Recupera totalmente a stamina
    def resetStamina(self):
        self.__currentStamina = self.__stamina
    
    # Altera a posição do jogador
    def setPosition(self, new_position):
        self.__position = new_position

    # Retorna a posição atual do jogador
    def getPosition(self):
        return self.__position
    
    # Atribui a chave ao jogador
    def setKey(self):
        self.__key = 1

    # Retorna se o jogador possui a chave
    def getKey(self):
        return self.__key