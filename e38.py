class Curso:
    def __init__(self, codcurso, nomecurso, codturma, coddisciplina):
        self.codcurso = codcurso
        self.nomecurso = nomecurso
        self.codturma = codturma
        self.coddisciplina = coddisciplina

    def montarcurso(self, codcurso):
        self.codcurso = codcurso 
    def organziarcurso(self, codturma):
        self.codturma = codturma
    def mostracurso(self):
        print(f'Codcurso: {self.codcurso}, Nome curso: {self.nomecurso}, codturma: {self.codturma}, coddisciplina: {self.coddisciplina}')
curso = Curso(1, 'TI- Programação', 2, 1)
curso.mostracurso()
curso.montarcurso(2)
curso.organziarcurso(4)

