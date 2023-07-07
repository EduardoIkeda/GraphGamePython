"""
Esse é o arquivo que inicia o jogo, ele que vai chamar as outras
classes para gerar as fases e o personagem.
"""

#Importação de Bibliotecas externas
import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Importação de arquivos nossos
from PlayerController import PlayerController
from Interface import Interface
from Player import Player
from Level import Level

# Variáveis globais
player = Player("Ikeda", 20, 20)
interface = Interface("Game of the year", player)

#Define o tamanho da fase (Quantidade de vertices)
# x = int(input("Digite o tamanho da fase:\n"))
x= 20 # PRECISA SER PAR
#Faz a criação do grafo
level = Level(x)
graph = level.generate_level(interface)

#Adiciona elementos de controle do jogador na interface
interface.createGameFrame()

# playerController = PlayerController(interface, player)

# Executar a janela do jogo
tk.mainloop()

#NOTA: ESTÁ FUNCIONANDO A GERAÇÃO DO GRAFO, A VISUALIZAÇÃO E A MOVIMENTAÇÃO. 
#ESTÁ FALTANDO IMPLEMENTAR AS REGRAS DE JOGO