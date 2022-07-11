Class Funcionario:

    def __init__(self, nome: str, CPf: str, salario: float, desconto: float, salarioliquido: float):

    self.nome = nome
    self.cpf = CPF  
    self.salarioliquido = salarioliquido
    self.desconto = desconto

    if descontar(self, salario, desconto):
        self.desconto = salario *0.05

    def liquidar(self, salario, desconto, salarioliquido):
        self.salarioliquido = salario - desconto 

    def mostrafuncionario(self):
        print(f'nome:{self.nome}, cpf: {self.cpf}, salarioliquido {self.salarioliquido}, desconto {self.desconto}')

os = Funcionario('marcos', '12222', 2500, 0.05, 2375)
os.mostrafuncionario()
os.descontar(3000,0.05)
os.liquidar(3000,1,1)
os.mostrarfuncionario()

