import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from PlayerController import PlayerController
from Interface import Interface
from Player import Player
from Level import Level

# Variáveis globais
player = Player("Ikeda", 20, 20)
interface = Interface("Game of the year", player)

x = int(input("Digite o tamanho da fase:\n"))

level = Level(x)
graph = level.generate_level(interface)

interface.createGameFrame()
print("fechou")
# playerController = PlayerController(interface, player)

# Executar a janela do jogo
tk.mainloop()


#NOTA: ESTÁ FUNCIONANDO A GERAÇÃO DO GRAFO E A VISUALIZAÇÃO. 
#ESTÁ FALTANDO FAZER FUNCIONAR A MOVIMENTAÇÃO USANDO CLASSES
#E IMPLEMENTAR AS REGRAS DE JOGO