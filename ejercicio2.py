from enum import Enum

class Tipo(Enum):
    V = "Vertebrado"
    I = "Invertebrado"

class Animal:
    def __init__(
            self, 
            cantidad_patas: int,
            tipo: str,
            ):
        self.cantidad_patas=cantidad_patas
        self.tipo=tipo
        
    def comer(self):
        print("Estoy comiendo")
    def imprimir(self):
        pass

class Perro(Animal):
    def __init__(
            self,
            cantidad_patas,
            tipo,
            nombre,
            raza
            ):
        self.nombre=nombre
        self.raza=raza
        super().__init__(cantidad_patas, tipo)
    def correr(self):
        print("Estoy corriendo")
    def imprimir(self):
        print(f'Cantidad de patas: {self.cantidad_patas}')
        print(f'Tipo: {self.tipo}')
        print(f'Nombre: {self.nombre}')
        print(f'Raza: {self.raza}')

class Aguila(Animal):
    def __init__(
            self,
            cantidad_patas,
            tipo            
            ):
        super().__init__(cantidad_patas, tipo)
    def volar(self):
        print("Estoy volando")

    def imprimir(self):
        print(f'Cantidad de patas: {self.cantidad_patas}')
        print(f'Tipo: {self.tipo}')



perro1 = Perro(5, Tipo.V.value, "Firulais", "Salchicha")
print(perro1.correr())
perro1.imprimir()


aguila1 = Aguila(2, Tipo.V.value)
print(aguila1.volar())
aguila1.imprimir()