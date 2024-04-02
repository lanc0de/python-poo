class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        self.moedas = 0
        self.ataque = 10
        self.nivel = 1
        
    def esquivar(self):
        print(f"{self.nome} esquivou!")
    
    def subir_nivel(self):
        self.nivel += 1
        self.ataque += 5
        print(f"{self.nome} subiu de nível!\nNível atual: {self.nivel}")
 
class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
    
    def usar_espada(self):
        print(f"{self.nome} usou a espada!")


class Curandeiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
    
    def curar(self, alvo:Personagem):
        alvo.vida += 10
        print(f"{self.nome} curou {alvo.nome}!")

kain = Guerreiro("Kain")
mei = Curandeiro("Mei")

kain.vida -= 20
print(kain.vida)

mei.curar(kain)

print(kain.vida)