
from Restaurante.cardapio import Cardapio

#super quer dizer que está tendo uma herança

class Bebidas(Cardapio):
    def __init__(self, nome, preco, tipo):
        super().__init__(nome,preco)
        self.tipo = tipo

    def __str__(self):
        return 'O nome da cliente é {} e o tipo é da bebida é {}'.format(self.nome, self.tipo)