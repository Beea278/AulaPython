class Cliente:
    def __init__(self,nome,idade,sexo,salario):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.salario = salario
       

    def getpreco (self):
        print ("O salario é", self.preco)
    #metodo para alterar o salário
    def setPreco(self, precoNovo):
        self.preco = precoNovo
        print("O novo preço do livro é", self.preco)

    mostrarlivro = property(getpreco, setPreco)
cliente = Cliente ("Pedro", 34, "Masculino", 6500.00)
cliente.getsalario()
cliente.setSalario(15)

print(vars(cliente))

