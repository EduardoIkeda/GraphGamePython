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
    def update_player_position(interface, player, new_position):
        graph = interface.graph
        # Verificar se o movimento é válido (se há uma aresta entre a posição atual e a nova posição)
        if graph.has_edge(player.getPosition(), new_position):
            terrainType = nx.get_node_attributes(graph, 'color')[new_position]
            edgeColor = nx.get_node_attributes(graph, 'edgecolor')[new_position]
    
            if("orange" == terrainType):
                staminaCost = 4
            elif("yellow" == terrainType):
                staminaCost = 2
            elif("white" == terrainType):
                staminaCost = 1

            #Perda de vida
            if(edgeColor == "red"):
                player.takeDamage(6)
            #Pegou chave
            elif(edgeColor == "purple"):
                player.setKey()

            if(player.getStamina() > staminaCost):
                player.setPosition(new_position)
                # Adicionar a nova posição e os nós adjacentes aos nós visíveis
                interface.addVisibleNodes(player.getPosition())
                # Atualiza o mapa para o jogador.

                if(edgeColor == "purple"):
                    nx.set_node_attributes(graph, {new_position: {'color': terrainType, 'edgecolor': "black"}})
                interface.refreshPlayerView(player.getPosition())
                # Altera a mensagem com a nova posição do jogador
                player.lossStamina(staminaCost)

                interface.refreshPlayerStatus()

                #Verifica se morreu
                if(player.getLife() <= 0):
                    interface.setPlayerMessage("O jogador morreu. Fim de jogo!")
                    interface.lockEntry()
                
                if(edgeColor == "purple"):
                    interface.setPlayerMessage("Você pegou a chave! Você está no lugar " + str(player.getPosition()))
                elif(edgeColor == "green" and player.getKey() == 0):
                    interface.setPlayerMessage("Você ainda não pegou a chave! Você está no lugar " + str(player.getPosition()))
                elif(edgeColor == "green" and player.getKey() == 1):
                    interface.setPlayerMessage("Você ganhou, parabéns!")
                    interface.lockEntry()
                elif(edgeColor == "white"):
                    interface.setPlayerMessage("Você está no lugar " + str(player.getPosition()))
            else:
                interface.setPlayerMessage("Stamina insuficiente!")    
        else:
            interface.setPlayerMessage("Movimento inválido!")
    
    def restPlayer(player, interface):
        player.resetLife()
        player.resetStamina()
        interface.refreshPlayerStatus()
        
