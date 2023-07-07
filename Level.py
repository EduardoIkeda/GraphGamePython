"""
Aqui você vai fazer tudo relacionado a fase do jogo, como o peso dos vértices,
a geraçao das fases, localização de chave e portao.
"""

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import random
from Interface import Interface

class Level:
    mountain = "orange"
    forest = "yellow"
    plains = "white"

    #Inicializa a fase com o tamanho dela
    def __init__(self, levelSize):
        self.levelSize = levelSize

    # Função para gerar o grafo aleatório
    def _generate_random_graph(self):
        # Criar um grafo vazio
        graph = nx.Graph()

        # Adicionar nós e arestas aleatórias ao grafo
        graph.add_node(1)  # Nó inicial

        terrain_choice = [self.plains, self.forest, self.mountain]
        edge_choice = []
        for i in range(0, (int(self.levelSize/2)) - 1): # red é inimigo, black é node normal, purple é chave, green é Portão
            edge_choice.append("black")
            
        for i in range(0, (int(self.levelSize/2)) - 1): # red é inimigo, black é node normal, purple é chave, green é Portão
            edge_choice.append("red")

        edge_choice.append("purple")
        edge_choice.append("green")
                
        size = len(edge_choice)

        
        for i in range(2, self.levelSize + 1):
            parent_node = random.randint(1, i - 1)  # Selecionar um nó pai aleatório
            graph.add_edge(parent_node, i)  # Adicionar aresta entre o nó pai e o novo nó

        for node in graph.nodes:
            if size>0 and node!=1:
                random_terrain = random.choice(terrain_choice)
                random_edge = random.randint(0, len(edge_choice)-1)
                edge_color = edge_choice.pop(random_edge)
                nx.set_node_attributes(graph, {node: {'color': random_terrain, 'edgecolor': edge_color}})
                size=size-1

        nx.set_node_attributes(graph, {1: {'color': self.plains, 'edgecolor': "black"}})

        return graph
    
    def getTerrainTypeColor(self):
        return self.plains, self.forest, self.mountain
    
    def getTerrainStaminaCost(self, attribute):
        if(attribute == self.plains):
            return 1
        elif(attribute == self.forest):
            return 2
        elif(attribute == self.mountain):
            return 4
        else:
            return 0

    def generate_level(self, interface: Interface):
        startNode = 1
        graph = self._generate_random_graph()
        interface.setupCreatedGraph(graph)
        interface.initVisibleNodes()

        interface.refreshPlayerView(startNode)

        return graph
