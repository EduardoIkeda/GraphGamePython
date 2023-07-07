"""
Aqui é feita a manipulação do personagem dentro do jogo, realizando as tratativas de verificar a disponibilidade de 
stamina para andar, se irá descansar e recuperar sua vida e stamina, se receberá dano, se o jogador morreu, 
pegou a chave ou terminou o jogo.
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

        # Verifica se o movimento é válido (se há uma aresta entre a posição atual e a nova posição)
        if graph.has_edge(player.getPosition(), new_position):
            # Recebe o tipo do terreno (cor) e o conteúdo (cor de borda) da nova posição
            terrainType = nx.get_node_attributes(graph, 'color')[new_position]
            contentType = nx.get_node_attributes(graph, 'edgecolor')[new_position]
    
            # Define o custo de stamina (peso) de cada terreno
            if("orange" == terrainType):
                staminaCost = 4
            elif("yellow" == terrainType):
                staminaCost = 2
            elif("white" == terrainType):
                staminaCost = 1

            # Verifica se o jogador possui stamina o suficiente para realizar o movimento
            if(player.getStamina() > staminaCost):
                # Movimenta o jogador
                player.setPosition(new_position)
                # Adiciona a nova posição e os nós adjacentes aos nós visíveis
                interface.addVisibleNodes(player.getPosition())
     
                # Altera a cor de borda da chave para preto, caso ela tenha sido adquirida pelo jogador
                if(contentType == "purple"):
                    nx.set_node_attributes(graph, {new_position: {'color': terrainType, 'edgecolor': "black"}})

                # Atualiza o mapa para o jogador.                    
                interface.refreshPlayerView(player.getPosition())
                
                # Perda de stamina
                player.lossStamina(staminaCost)

                # Perda de vida
                if(contentType == "red"):
                    player.takeDamage(6)

                # Pegou chave
                elif(contentType == "purple"):
                    player.setKey()

                # Atualiza a vida e a stamina
                interface.refreshPlayerStatus()

                # Verifica se morreu
                if(player.getLife() <= 0):
                    interface.setPlayerMessage("O jogador morreu. Fim de jogo!")
                    interface.lockEntry()
                
                # Altera a mensagem com a nova posição do jogador
                if(contentType == "purple"):
                    interface.setPlayerMessage("Você pegou a chave! Você está no lugar " + str(player.getPosition()))
                elif(contentType == "green" and player.getKey() == 0):
                    interface.setPlayerMessage("Você ainda não pegou a chave! Você está no lugar " + str(player.getPosition()))
                elif(contentType == "green" and player.getKey() == 1):
                    interface.setPlayerMessage("Você ganhou, parabéns!")
                    interface.lockEntry()
                elif(contentType == "black"):
                    interface.setPlayerMessage("Você está no lugar " + str(player.getPosition()))
            else:
                interface.setPlayerMessage("Stamina insuficiente!")    
        else:
            interface.setPlayerMessage("Movimento inválido!")
    
    # Função para recuperar vida e stamina ao máximo
    def restPlayer(player, interface):
        player.resetLife()
        player.resetStamina()
        interface.refreshPlayerStatus()
        
