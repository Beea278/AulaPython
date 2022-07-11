class Aluno:
    def __init__(self, matricula, nome, codturma):
        self.matricula = int (matricula)
        self.nome = str (nome)
        self.codturma = int (codturma)
    def acessarcadastro(self, matricula):
        self.matricula = matricula
    def realizarmatricula(self, nome):
        self.nome = nome
    def participaraula(self, matricula):
        self.matricula = matricula
    def mostraAluno(self):
        print(f'Matricula: {self.matricula}, Nome: {self.nome}, codturma: {self.codturma}')
    Aluno = Aluno(123545, 'Ana', 2)
Aluno.mostraAluno()
Aluno.participaraula(12345)
Aluno.acessarcadastro(1)
Aluno.realizarmatricula('Pedro')
Aluno.mostraAluno()