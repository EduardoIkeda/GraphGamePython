"""
Aqui você vai fazer a manipulação do personagem dentro do jogo, fazendo
as tratativas de verificar se tem energia pra andar, se vai recuperar 
energia se vai atacar, morrer, terminar o jogo.
"""

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import random

class PlayerController:
    # Função para atualizar a posição do jogador
    def update_player_position(interface,player, new_position):
        graph = interface.graph
        # Verificar se o movimento é válido (se há uma aresta entre a posição atual e a nova posição)
        if graph.has_edge(player.getPosition(), new_position):
            player.setPosition(new_position)

            # Adicionar a nova posição e os nós adjacentes aos nós visíveis
            interface.addVisibleNodes(player.getPosition())

            # Atualiza o mapa para o jogador.
            interface.refreshPlayerView(player.getPosition())

            # Altera a mensagem com a nova posição do jogador
            interface.setPlayerMessage("Você está no lugar " + str(player.getPosition()))
        else:
            interface.setPlayerMessage(text="Movimento inválido!")
    
    def restPlayer(self):
        teste = 1