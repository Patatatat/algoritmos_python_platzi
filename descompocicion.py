class Automovil:
    
    def __init__(self, modelo, color, marca):
        self.modelo = modelo
        self.color = color
        self.marca = marca
        self._estado = 'en reposo'
        self._motor = Motor(cilindros=4)

    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

        self._estado = 'Encendido'

class Motor:

    def __init__(self, cilindros, tipo='gasolina') -> None:
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad_limite):
        pass