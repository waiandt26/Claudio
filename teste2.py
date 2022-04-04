#coding: utf-8

vertice = int(input('Digite a quantidade de vertices do Grafo: '))
lista = [[0] * vertice for i in range(vertice)]
print (lista)


arrestas = int(input('Digite a quantidade de arrestas do Grafo: '))
for i in range(arrestas):
      v = int(input('De qual vértice parte esta aresta? '))
      a = int(input('Para qual vértice chega esta aresta? '))
      lista[v-1].append(a-1)

print (lista)
