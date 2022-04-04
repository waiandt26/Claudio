class Busca_Grafo:
    def __init__ (self, vertices):
        self.dic_vert = {}
        for i in range(1, vertices + 1):
            print('Digite 0 para terminar a quantidade de arrestas de ligações do vertice')
            x = 1
            lista = []
            while x != 0:
                arresta = int(input('Digite para qual vertice %i faz ligação: ' % i))
                if arresta != 0:
                    lista.append(arresta)
                x = arresta
            self.dic_vert[i] = lista
        print(self.dic_vert)

vertices = int(input('Digite a quantidade de vertices: '))
grafo = Busca_Grafo(vertices)
