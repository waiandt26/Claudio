# BFS - Algoritmo para Busca em Largura
# https://www.youtube.com/watch?v=mFb8WwI98b0

# importa a biblioteca para poder criar uma lista
from collections import defaultdict


# classe para criação do grafo direcionado e que usa representação de lista de adjacência
class Graph:

    # constroi a função que ira criar a lista
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = [[0] * self.vertices for i in range(self.vertices)]

        # Quando você cria um defaultdict, fornece uma função usada para criar valores, nesse caso criou-se a lista
        ##self.graph = defaultdict(list)

        # função que adiciona os vértices no grafo

    def adiciona_aresta(self, u, v):
        #self.graph[u].append(v)
        self.graph[u-1][v-1]

        # função para imprimir a BFS do grafo, recebe o primeiro nó a ser visitado

    def BFS(self, s):

        # marca todos os vértices como não visitados.
        visited = [False] * (len(self.graph))

        # cria uma fila vazia para o BFS
        queue = []

        # pega o nó de origem, marca como visitado e insere ele na fila
        queue.append(s)
        visited[s] = True

        # enquanto a fila não for vazia
        while queue:

            # retira o último vértice inserido na fila e imprime
            s = queue.pop(0)
            print(s, " ")

            # Obtenha todos os vértices adjacentes dos vértices desenfileirados. Se um adjacente não foi visitado, marque-o como visitado e coloque-o na fila
            for i in self.graph[s]:
                # print(visited[i])
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


# Criação do grafo
##g = Graph()

v = int(input('Digite a quantidade de vértices: '))
g = Graph(v)

a = int(input('Digite a quantidade de arestas:  '))
for i in range(a):
    x = int(input('De qual vértice parte esta aresta? '))
    y = int(input('Para qual vértice chega esta aresta? '))
    g.adiciona_aresta(x,y)


t = int(input('Digite o vertice a começar a busca:  '))
print("Segue a execução da Busca em Largura, começando pelo vértice", t)
g.BFS(t)

