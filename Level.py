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
    # Cores dos terrenos
    plains = "white"
    forest = "yellow"
    mountain = "orange"
    # Cores dos conteúdos (o que tem dentro do nodo)
    normal = "black"
    enemy = "red"
    key = "purple"
    gate = "green"
    
    # Inicializa a fase com o tamanho dela
    def __init__(self, levelSize):
        self.levelSize = levelSize

    # Função para gerar o grafo aleatório
    def _generate_random_graph(self):
        # Cria um grafo vazio
        graph = nx.Graph()

        # Adiciona nós e arestas aleatórias ao grafo
        graph.add_node(1)  # Nó inicial
        for i in range(2, self.levelSize + 1):
            parent_node = random.randint(1, i - 1)  # Selecionar um nó pai aleatório
            graph.add_edge(parent_node, i)  # Adicionar aresta entre o nó pai e o novo nó

        # Define vetores para escolha de atributos
        terrain_choice = [self.plains, self.forest, self.mountain]
        content_choice = []
        for i in range(0, (int(self.levelSize/2)) - 1):
            content_choice.append(self.normal) 
        for i in range(0, (int(self.levelSize/2)) - 1):
            content_choice.append(self.enemy)
        content_choice.append(self.key)
        content_choice.append(self.gate)
                
        size = len(content_choice)

        # Define os atributos de cada nodo
        nx.set_node_attributes(graph, {1: {'color': self.plains, 'edgecolor': self.normal}}) # Nó inicial
        for node in graph.nodes:
            if size>0 and node!=1:
                random_terrain = random.choice(terrain_choice)
                random_content = random.randint(0, len(content_choice)-1)
                content = content_choice.pop(random_content)
                if (content == self.key):
                    self.keyLocation = node
                elif (content == self.gate):
                    self.endLocation = node
                nx.set_node_attributes(graph, {node: {'color': random_terrain, 'edgecolor': content}})
                size=size-1

        return graph
    
    def getTerrainTypeColor(self):
        return self.plains, self.forest, self.mountain
    
    # Retorna o custo de stamina de cada terreno
    def getTerrainStaminaCost(self, attribute):
        if(attribute == self.plains):
            return 1
        elif(attribute == self.forest):
            return 2
        elif(attribute == self.mountain):
            return 4
        else:
            return 0

    # Controla a criação do grafo
    def generate_level(self, interface: Interface):
        startNode = 1
        graph = self._generate_random_graph()
        interface.setupCreatedGraph(graph)
        interface.initVisibleNodes()
        
        interface.setLocation(self.endLocation)
        interface.setKey(self.keyLocation)

        interface.refreshPlayerView(startNode)

        return graph
