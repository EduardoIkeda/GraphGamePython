import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import random

class PlayerController:
    # def __init__(self):
        

    # Função para atualizar a posição do jogador
    def update_player_position(interface, player, new_position):
        graph = interface.graph

        # Obter o valor digitado no campo de entrada
        # new_position = self.interface.getMoveEntry()

        # Verificar se o movimento é válido (se há uma aresta entre a posição atual e a nova posição)
        if graph.has_edge(player.getPosition(), new_position):
            player.setPosition(new_position)

            # Adicionar a nova posição e os nós adjacentes aos nós visíveis
            interface.addVisibleNodes(player.getPosition())

            interface.refreshPlayerView(player.getPosition())

            # Exibir mensagem para o jogador
            interface.setPlayerMessage("Você está no lugar " + str(player.getPosition()))
        else:
            interface.setPlayerMessage(text="Movimento inválido!")