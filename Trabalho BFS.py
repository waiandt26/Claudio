## Grafo é representado por: Vertices V e arestas A // G = (V,E)


class Busca_Grafo:
     ##'''Criando a estrutra da matriz que vai representar o grafo'''
     def __init__(self,vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]

     ##'''Craindo estrutura para adicionar as arestas'''

     def adiciona_aresta(self, u, v):
        self.grafo[v-1][u-1] = v
        ##self.grafo[u].append(v)
        ##self.grafo[u].[v] = v

     def mostra_matriz(self):
         print('A matriz de adjacências é:')
         for i in range(self.vertices):
             print(self.grafo[i])

     def busca_largura(self, s):
        # marca todos os vértices como não visitados.
        visitado = [False] * (len(self.grafo))

        # cria uma fila vazia para o BFS
        fila = []

        # pega o nó de origem, marca como visitado e insere ele na fila
        fila.append(s)
        visitado[s] = True

        # enquanto a fila não for vazia
        while fila:

            # retira o último vértice inserido na fila e imprime
            s = fila.pop(0)
            print(s, " ")

            # Obtenha todos os vértices adjacentes dos vértices desenfileirados. Se um adjacente não foi visitado, marque-o como visitado e coloque-o na fila
            for i in self.grafo[s]:
                # print(visitado[i])
                if visitado[i] == False:
                    fila.append(i)
                    visitado[i] = True


vertice = int(input('Digite a quantidade de vértices: '))
g = Busca_Grafo(vertice)
g.mostra_matriz()

aresta = int(input('Digite a quantidade de arestas: '))

for i in range(aresta):
    u = int(input('De qual vértice parte esta aresta? '))
    v = int(input('Para qual vértice chega esta aresta? '))
    g.adiciona_aresta(u, v)

g.mostra_matriz()

exec_vert = int(input('Digite a partir de qual vertice será feita a pesquisa: '))
print("Segue a execução da Busca por Largura, começando pelo vértice: " + str(exec_vert))
g.busca_largura(exec_vert)

