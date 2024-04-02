class Pessoa:
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero

class Professor(Pessoa):
    def __init__(self, nome, idade, genero, especialidade, salario):
        super().__init__(nome, idade, genero)

        self.especialidade = especialidade
        self.salario = salario

class Aluno(Pessoa):
    def __init__(self, nome, idade, genero, curso, periodo):
        super().__init__(nome, idade, genero)

        self.curso = curso
        self.periodo = periodo
        
claudio = Professor("Cláudio", 43, "M", "Doutor em Psicologia", 4000)
rafaela = Aluno("Rafaela", 19, "F", "Engenharia", 2)

print(claudio.especialidade)
print(rafaela.idade)