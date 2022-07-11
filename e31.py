class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.nivelcombustivel = 0 

    def andar(self, distancia):
        temp = distancia/self.consumo
        self.nivelcombustivel -= temp

    def obterGasolina(self):
        return self.nivelcombustivel

    def adiconarGasolina(self, qtd):
        self.nivelcombustivel += qtd

meuFusca = Carro(8)
meuFusca.adicionarGasolina(50)
meuFusca.andar(300)

