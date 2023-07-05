"""
Esse arquivo você não precisa commitar, vai servir pra você ficar fazendo testes
de funções ou bibliotecas etc... Vou até deixar ele no git ignore
"""

import tkinter as tk
from tkinter import ttk

# Criar uma janela
root = tk.Tk()

# Criar um frame
frame = tk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10)

# Adicionar um ProgressBar
progressbar = ttk.Progressbar(frame, mode='indeterminate')
progressbar.grid(row=0, column=0, pady=10)

# Adicionar um Button
button = ttk.Button(frame, text='Clique aqui')
button.grid(row=1, column=0, pady=10)

# Adicionar uma Entry
entry = ttk.Entry(frame)
entry.grid(row=2, column=0, pady=10)

# Iniciar a janela
root.mainloop()



# import tkinter as tk
# from tkinter import ttk

# # Função para alterar a cor da barra de progresso
# def change_progressbar_color(progressbar, color):
#     style = ttk.Style()
#     style.theme_use('default')

#     # Definir a cor do fundo da barra de progresso
#     style.configure('1.Horizontal.TProgressbar',
#         background=color)
    
#     style.configure('2.Horizontal.TProgressbar',
#         background='blue')

# # Criar uma janela
# root = tk.Tk()

# # Criar a barra de progresso
# progressbar = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=200, mode='determinate', style="1.Horizontal.TProgressbar")
# progressbar.pack()

# progressbar2 = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=200, mode='determinate', style="2.Horizontal.TProgressbar")
# progressbar2.pack()

# # Definir os valores iniciais e máximos da barra de progresso
# initial_value = 50
# progressbar['value'] = initial_value
# progressbar['maximum'] = 100

# progressbar2['value'] = initial_value
# progressbar2['maximum'] = 100

# # Mudar a cor da barra de progresso
# change_progressbar_color(progressbar, 'red')

# # Iniciar a janela
# root.mainloop()


# """
# Aqui você vai fazer qualquer alteração que esteja relacionada com atualização
# da interface ou a execução de botões por meio da interface
# """

# import tkinter as tk
# from tkinter import ttk
# import networkx as nx
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from PlayerController import PlayerController

# class Interface:
    
#     move_entry = None
#     move_button = None

#     def __init__(self, gameTitle, player):
#         # Declara o player para poder pegar as variáveis de vida e stamina para atualizar a interface
#         self.player = player

#         # Root é a janela da interface, dentro dela vão os frames
#         self.root = tk.Tk()
#         self.root.title = gameTitle

#         self.root.set

#         self.style = ttk.Style()

#         # # Criar as barras de progresso personalizadas
#         # progress_bar1 = ttk.Progressbar(self.root, orient=tk.HORIZONTAL, length=200, mode='determinate', style='1.Horizontal.TProgressbar')
#         # progress_bar1.pack()

#         # progress_bar2 = ttk.Progressbar(self.root, orient=tk.HORIZONTAL, length=200, mode='determinate', style='2.Horizontal.TProgressbar')
#         # progress_bar2.pack()

#         # self.configureInterfaceBarStyle()

#         # Mensagem para o usuário, por enquanto identifica a casa atual dele
#         self.playerMessage = tk.Label(self.root, text="Você está no lugar 1")
#         self.playerMessage.pack()

#         # Criar figura e plotar o grafo inicial
#         self.fig = plt.figure(figsize=(5, 5))
#         self.ax = self.fig.add_subplot(111)

#         # Criar canvas para exibir o grafo
#         self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
#         self.canvas.get_tk_widget().pack()

        
    
#     def configureInterfaceBarStyle(self):
#         self.style.configure('healthBar.Horizontal.TProgressbar',
#         background='red')
    
#         self.configure('staminaBar.Horizontal.TProgressbar',
#             background='yellow')

#     def createGameFrame(self):
#         #Cria o quadro em que vão ser inserido os botões
#         self.game = tk.Frame(self.root)

#         # self.healthbar = ttk.Progressbar(self.game, orient=tk.HORIZONTAL, length=200, mode='determinate', style='Custom.Horizontal.TProgressbar1')
#         # self.healthbar.pack()
#         # self.healthbar['value'] = 100

#         # self.staminabar = ttk.Progressbar(self.game, orient=tk.HORIZONTAL, length=200, mode='determinate', style='Custom.Horizontal.TProgressbar2')
#         # self.staminabar.pack()
#         # self.staminabar['value'] = 100

#         # Criar campo de entrada para movimentar o jogador
#         self.move_entry = tk.Entry(self.game)
#         self.move_entry.pack(side=tk.LEFT)

#         # Criar botão para movimentar o jogador
#         self.move_button = tk.Button(self.game, text="Mover", command=self.requestPlayerController)
#         self.move_button.pack(side=tk.LEFT)

#         self.game.pack()

#     def requestPlayerController(self):
#         # Pega o valor do campo de texto da interface e atribui como nova posição
#         new_position = self.move_entry.get()

#         # Verifica se é um número
#         if new_position.isdigit():
#             new_position = int(new_position)
#             # Solicita atualização da posição do jogador no grafo
#             PlayerController.update_player_position(self, self.player, new_position)
#         else:
#             print("Valor inválido!")

#     # Muda a mensagem que aparece pro jogador
#     def setPlayerMessage(self, message):
#         self.playerMessage.configure(text=message)
    
#     # Inicializa o grafo configurando o node inicial e seus vizinhos como visiveis
#     def initVisibleNodes(self):
#         self.visible_nodes = set([1])
#         self.visible_nodes.update(self.graph.neighbors(1))

#     # Depois de inicializado, ele faz só a adição de mais vértices aos nodes visíveis
#     def addVisibleNodes(self, value):
#         self.visible_nodes.add(value)
#         self.visible_nodes.update(self.graph.neighbors(value))

#     # Atualiza o grafo exibido para o jogador
#     def refreshPlayerView(self, playerPosition):
#         # Limpar o grafo anterior
#         self.ax.clear()

#         node_colors = nx.get_node_attributes(self.graph, 'color')
        
#         # Atualiza o novo grafo
#         nx.draw(self.graph.subgraph(self.visible_nodes), self.node_position, with_labels=True, ax=self.ax)
#         nx.draw_networkx_nodes(self.graph, self.node_position, nodelist=self.visible_nodes, node_color=[node_colors[node] for node in self.visible_nodes], node_size=500)
#         nx.draw_networkx_nodes(self.graph, self.node_position, nodelist=[playerPosition], node_color='blue', node_size=500)

#         # Atualizar a janela com o novo grafo
#         self.canvas.draw()

#     # atribui a interface o grafo gerado pelo level e a posição dos vértices na tela
#     def setupCreatedGraph(self, graph):
#         self.graph = graph
#         self.node_position = nx.spring_layout(self.graph)