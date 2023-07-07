#Aqui é feito o controle da atualização da interface e da execução de botões por meio da interface

import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PlayerController import PlayerController

class Interface:
    def __init__(self, gameTitle, player):
        # Declara o player para poder pegar as variáveis de vida e stamina para atualizar a interface
        self.player = player
        self.key = None
        self.location = None

        # Root é a janela da interface, dentro dela vão os frames
        self.root = tk.Tk()
        self.style = ttk.Style()
        self.root.title = gameTitle

        # Mensagem para o usuário, por enquanto identifica a casa atual dele
        self.playerMessage = tk.Label(self.root, text="Você está no lugar 1")
        self.playerMessage.pack()

        # Cria figura e plota o grafo inicial
        self.fig = plt.figure(figsize=(5, 5))
        self.ax = self.fig.add_subplot(111)

        # Cria canvas para exibir o grafo
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack()

    def createGameFrame(self):
        # Cria o quadro em que vão ser inserido os botões
        self.healthStatus = tk.Frame(self.root, width=500, height=15)
        self.staminaStatus = tk.Frame(self.root, width=500, height=10)
        self.playerController = tk.Frame(self.root, width=500, height=30)
        self.distances = tk.Frame(self.root, width=500, height=30)

        # Cria a barra de vida
        self.healthbar = ttk.Progressbar(self.healthStatus, orient=tk.HORIZONTAL, length=200, mode='determinate', style='health.Horizontal.TProgressbar')
        self.healthbar.pack(side="left")
        self.healthtext = tk.Label(self.healthStatus)
        self.healthtext.pack(side="left")

        # Cria a barra de stamina
        self.staminabar = ttk.Progressbar(self.staminaStatus, orient=tk.HORIZONTAL, length=200, mode='determinate', style='stamina.Horizontal.TProgressbar')
        self.staminabar.pack(side="left")
        self.staminatext = tk.Label(self.staminaStatus)
        self.staminatext.pack(side="left")

        # Cria os labels informativos de distância
        self.keytext = tk.Label(self.distances)
        self.keytext.pack()
        self.locationtext = tk.Label(self.distances)
        self.locationtext.pack()

        self.refreshPlayerStatus()
        self.healthbar['maximum'] = self.player.getLife()
        self.staminabar['maximum'] = self.player.getStamina()

        # Preenchimento das barras de vida e stamina
        self.style.theme_use('default')
        self.style.configure('health.Horizontal.TProgressbar',
            thickness=15,
            background='red')
        self.style.configure('stamina.Horizontal.TProgressbar',
            thickness=10,
            background='yellow')

        # Cria campo de entrada para movimentar o jogador
        self.move_entry = tk.Entry(self.playerController)
        self.move_entry.pack(side=tk.LEFT)

        # Cria botão para movimentar o jogador
        self.move_button = tk.Button(self.playerController, text="Mover", command=self.requestPlayerControllerPosition)
        self.move_button.pack(side=tk.LEFT)

        # Cria botão para descansar o jogador
        self.rest_button = tk.Button(self.playerController, text="Descansar", command=self.requestPlayerControllerRest)
        self.rest_button.pack(side=tk.BOTTOM)
        
        # Decide o posicionamento de cada frame
        self.healthStatus.pack(side = "left")
        self.staminaStatus.pack(side = "left")
        self.playerController.pack(side = "right")
        self.distances.pack(side="bottom")
        

    def requestPlayerControllerPosition(self):
        # Pega o valor do campo de texto da interface e atribui como nova posição
        new_position = self.move_entry.get()

        # Verifica se é um número
        if new_position.isdigit():
            new_position = int(new_position)
            # Solicita atualização da posição do jogador no grafo
            PlayerController.update_player_position(self, self.player, new_position)
        else:
            self.setPlayerMessage("Valor inválido!")

    def requestPlayerControllerRest(self):
        PlayerController.restPlayer(self.player, self)

    # Atribui a interface o grafo gerado pelo level e a posição dos vértices na tela
    def setupCreatedGraph(self, graph):
        self.graph = graph
        self.node_position = nx.spring_layout(self.graph)

    # Inicializa o grafo configurando o node inicial e seus vizinhos como visiveis
    def initVisibleNodes(self):
        self.visible_nodes = set([1])
        self.visible_nodes.update(self.graph.neighbors(1))

    # Depois de inicializado, ele faz só a adição de mais vértices aos nodes visíveis
    def addVisibleNodes(self, value):
        self.visible_nodes.add(value)
        self.visible_nodes.update(self.graph.neighbors(value))

    # Atualiza o grafo exibido para o jogador
    def refreshPlayerView(self, playerPosition):
        # Limpa o grafo anterior
        self.ax.clear()

        node_colors = nx.get_node_attributes(self.graph, 'color')
        node_edges = nx.get_node_attributes(self.graph, 'edgecolor')
        
        # Atualiza o novo grafo
        nx.draw(self.graph.subgraph(self.visible_nodes), self.node_position, with_labels=True, ax=self.ax)
        nx.draw_networkx_nodes(self.graph, self.node_position, nodelist=self.visible_nodes, node_color=[node_colors[node] for node in self.visible_nodes], node_size=500, edgecolors=[node_edges[node] for node in self.visible_nodes], linewidths=2)
        nx.draw_networkx_nodes(self.graph, self.node_position, nodelist=[playerPosition], node_color='blue', node_size=500, edgecolors=node_edges[playerPosition], linewidths=2)

        # Atualiza a janela com o novo grafo
        self.canvas.draw()

    # Atualiza as interfaces de vida, stamina e distância
    def refreshPlayerStatus(self):
        self.healthbar['value'] = self.player.getLife()
        self.staminabar['value'] = self.player.getStamina()
        self.healthtext['text'] = self.player.getLife()
        self.staminatext['text'] = self.player.getStamina()
        self.keytext['text'] = "Chave: " + str(nx.shortest_path_length(self.graph, source=self.player.getPosition(), target=self.key))
        self.locationtext['text'] = "Saída: " + str(nx.shortest_path_length(self.graph, source=self.player.getPosition(), target=self.location))

    # Muda a mensagem que aparece pro jogador
    def setPlayerMessage(self, message):
        self.playerMessage.configure(text=message)

    # Bloqueia a interação com o jogador
    def lockEntry(self):
        self.move_entry.config(state="disabled")
        self.move_entry.pack(side=tk.LEFT)

        self.move_button.config(state="disabled")
        self.move_button.pack(side=tk.LEFT)

        self.rest_button.config(state="disabled")
        self.rest_button.pack(side=tk.BOTTOM)

    # Define o nodo que está com a chave
    def setKey(self, value):
        self.key = value

    # Define o nodo que está com o portão
    def setLocation(self, value):
        self.location = value

    

    