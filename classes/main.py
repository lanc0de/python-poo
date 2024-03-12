class Carro:
    def __init__(self, modelo, placa, cor):
        self.modelo = modelo
        self.placa = placa
        self.cor = cor
        self.gasolina = 100
        self.esta_ligado = False

    def ligar(self):
        if self.esta_ligado:
            print(f"O carro já está ligado.")
        else:
            self.esta_ligado = True
            print(f"{self.modelo} ligou.")

    def desligar(self):
        if self.esta_ligado:
            self.esta_ligado = False
            print(f"{self.modelo} desligou.")
        else:
            print(f"O carro já está desligado.")
    
    def andar(self):
        if not self.esta_ligado:
            print(f"O carro precisa estar ligado para andar!")
            return
        if self.gasolina < 10:
            print("Sem gasolina!")
            return
        if self.esta_ligado and self.gasolina >= 10:
            print(f"{self.modelo} andou!")
            self.gasolina-=10

celta = Carro('Celta', 'uwu-90', 'Preto')
uno = Carro('Fiat Uno', 'Cimento-784', 'Rosa')

celta.ligar()
celta.andar()
print(celta.gasolina)
celta.andar()
print(celta.gasolina)
celta.desligar()
