import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PlayerController import PlayerController

class Interface:

    def __init__(self, gameTitle, player):
        self.player = player

        self.root = tk.Tk()
        self.root.title = gameTitle
        self.playerMessage = tk.Label(self.root, text="Você está no lugar 1")
        self.playerMessage.pack()

        # Criar figura e plotar o grafo inicial
        self.fig = plt.figure(figsize=(5, 5))
        self.ax = self.fig.add_subplot(111)

        # Criar canvas para exibir o grafo
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack()
        
        self.move_entry = None
        self.move_button = None

    def createGameFrame(self):
        self.game = tk.Frame(self.root)
        # Criar campo de entrada para movimentar o jogador
        self.move_entry = tk.Entry(self.game)
        self.move_entry.pack(side=tk.LEFT)

        # Criar botão para movimentar o jogador
        self.move_button = tk.Button(self.game, text="Mover", command=self.requestPlayerController)
        self.move_button.pack(side=tk.LEFT)
        self.game.pack()

    def requestPlayerController(self):
        new_position = self.move_entry.get()
        if new_position.isdigit():
            new_position = int(new_position)
            print(new_position)
            PlayerController.update_player_position(self, self.player, new_position)
        else:
            print("Valor inválido!")

    def setPlayerMessage(self, message):
        self.playerMessage.configure(text=message)
    
    def initVisibleNodes(self):
        self.visible_nodes = set([1])
        self.visible_nodes.update(self.graph.neighbors(1))

    def addVisibleNodes(self, value):
        # self.visible_nodes = set([value])
        self.visible_nodes.add(value)
        self.visible_nodes.update(self.graph.neighbors(value))

    def refreshPlayerView(self, playerPosition):
        # Limpar o plot anterior
        self.ax.clear()
        
        # Plotar o grafo inicial
        nx.draw(self.graph.subgraph(self.visible_nodes), self.node_position, with_labels=True, ax=self.ax)
        nx.draw_networkx_nodes(self.graph, self.node_position, nodelist=[playerPosition], node_color='r')

        # Atualizar a janela
        self.canvas.draw()

    def setCreatedGraph(self, graph):
        self.graph = graph
        self.node_position = nx.spring_layout(self.graph)