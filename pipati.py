import random


class PiPaTi:
    PIEDRA = "1"
    PAPEL = "2"
    TIJERA = "3"

    OPCIONES = [PIEDRA, PAPEL, TIJERA]

    GANO = "Ganaste"
    EMPATO = "Empatamos"
    PERDIO = "Perdiste"

    def __init__(self):
        self._opcion = self._elegir()

    def _elegir(self):
        return random.choice(self.OPCIONES)

    def _resolver_piedra(self):
        if self._opcion == self.TIJERA:
            return self.GANO
        if self._opcion == self.PAPEL:
            return self.PERDIO

    def _resolver_papel(self):
        if self._opcion == self.PIEDRA:
            return self.GANO
        if self._opcion == self.TIJERA:
            return self.PERDIO

    def _resolver_tijera(self):
        if self._opcion == self.PAPEL:
            return self.GANO
        if self._opcion == self.PIEDRA:
            return self.PERDIO

    def vs_maquina(self, jugador):
        if jugador == self._opcion:
            return self.EMPATO
        if jugador == self.PIEDRA:
            return self._resolver_piedra()
        if jugador == self.PAPEL:
            return self._resolver_papel()
        if jugador == self.TIJERA:
            return self._resolver_tijera()
