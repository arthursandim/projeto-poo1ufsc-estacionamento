#Arthur Vinicius Gouvea Sandim
#21204602
class Veiculo:
    def __init__(self, marca, modelo, cor, placa, dono):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.placa = placa
        self.dono = dono
        
    def getMarca(self):
        return self.marca
    def getModelo(self):
        return self.modelo
    def getCor(self):
        return self.cor
    def getPlaca(self):
        return self.placa
    def getDono(self):
        return self.dono
    
    def setMarca(self, nova_marca):
        self.marca = nova_marca
    def setModelo(self, novo_modelo):
        self.modelo = novo_modelo
    def setCor(self, nova_cor):
        self.cor = nova_cor
    def setPlaca(self, nova_placa):
        self.placa = nova_placa
    def setDono(self, novo_dono):
        self.dono = novo_dono

    
class Carro(Veiculo):#herança
    def __init__(self, marca, modelo, cor, placa, dono):
        super().__init__(marca, modelo, cor, placa, dono)
        self.tipo = 'Carro'
    
    def getTipo(self):
        return self.tipo

    def setTipo(self, novo_tipo):
        self.tipo = novo_tipo
        
    def mostra_dados(self):#polimorfismo
        print()
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")
        print(f"Placa: {self.placa}")
        print(f"Proprietário: {self.dono}")
        print()


class Moto(Veiculo):#herança
    def __init__(self, marca, modelo, cor, placa, dono):
        super().__init__(marca, modelo, cor, placa, dono)
        self.tipo = 'Moto'
    
    def getTipo(self):
        return self.tipo

    def setTipo(self, novo_tipo):
        self.tipo = novo_tipo
        
    def mostra_dados(self):#polimorfismo
        print()
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")
        print(f"Placa: {self.placa}")
        print(f"Proprietário: {self.dono}")
        print()
