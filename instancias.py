class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return(x_diff + y_diff)**0.5

if __name__ == '__main__':
    coordenada_1 = Coordenada(40, 10)
    coordenada_2 = Coordenada(10, 40)

    #print(coordenada_1.distancia(coordenada_2))
    print(isinstance(coordenada_2, Coordenada))