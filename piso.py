class Celdas():
    def __init__(self, indice, posicion, agente=False, basura=False):
        self.indice = indice
        self.posicion = posicion       # Arreglo [x,y]
        self.agente = False
        self.basura = False
        self.inicial = False

        self.izquierda = None
        self.derecha = None
        self.arriba = None
        self.abajo = None


    def matrizPosiciones(Options):
        M = Options.M
        N = Options.N

        matriz = []
        indice = 0

    # Espacios de la matriz
        for i in range(M):
            fila = []
            for j in range(N):
                posicion = (i, j)
                celda = Celdas(indice=indice, posicion=posicion)
                fila.append(celda)
                indice += 1
            matriz.append(fila)


    # Celdas adyacentes
        for i in range(M):
            for j in range(N):
                celda = matriz[i][j]
                if j > 0:
                    celda.izquierda = matriz[i][j - 1]
                if j < N - 1:
                    celda.derecha = matriz[i][j + 1]
                if i > 0:
                    celda.arriba = matriz[i - 1][j]
                if i < M - 1:
                    celda.abajo = matriz[i + 1][j]

        return matriz

    
    def celdaInicial(self, indice, Options):
        if Options.CeldaInicial == indice: 
            self.inicial = True





