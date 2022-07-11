from mailbox import NotEmptyError


class pessoa:
    def __init__(self, nome: str, idade: int, peso: float, altura: float):
           self.nome = nome
           self.idade = idade
           self.peso = peso
           self.altura = altura

           def engordar (self, peso):
               self.peso += peso

           def emagrecer(self):
               self.idade

           def crescer (self, altura):
                self.altura += altura

           def envelhecer(self, idade):
                if (self. idade<21):
                  self.altura += 0.5
def mostrapessoa(self):
    print(f'nome: {self.nome}, idade: {self.idade} anos, peso: {self.peso}kg, altura: {self.altura}cm')

    ana = pessoa('ana', 19, 54, 163)
    ana.mostrapessoa()

    ana.envelhecer(1)
    ana.engordar(3)
    ana. emagrecer(3)
    ana.crescer(1)
    ana.mostrapessoa(1)


        

