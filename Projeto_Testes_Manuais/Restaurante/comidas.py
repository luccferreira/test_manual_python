
from Restaurante.cardapio import Cardapio

class Comidas(Cardapio):
    def __init__(self, nome, preco, prato):
        super().__init__(nome, preco)
        self.prato = prato

    def __str__(self):
        return 'O nome da cliente é {} e o prato é {}'.format(self.nome, self.prato)