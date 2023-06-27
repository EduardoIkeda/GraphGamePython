import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import random
from Interface import Interface

class Level:
    def __init__(self, levelSize):
        self.levelSize = levelSize

    # Função para gerar o grafo aleatório
    def _generate_random_graph(self):
        # Criar um grafo vazio
        graph = nx.Graph()

        # Adicionar nós e arestas aleatórias ao grafo
        graph.add_node(1)  # Nó inicial
        
        for i in range(2, self.levelSize + 1):
            parent_node = random.randint(1, i - 1)  # Selecionar um nó pai aleatório
            graph.add_edge(parent_node, i)  # Adicionar aresta entre o nó pai e o novo nó

        return graph
    
    def refreshLevel():
        teste = 1

    def generate_level(self, interface: Interface):
        startNode = 1
        graph = self._generate_random_graph()
        interface.setCreatedGraph(graph)
        interface.initVisibleNodes()

        interface.refreshPlayerView(startNode)

        return graph
