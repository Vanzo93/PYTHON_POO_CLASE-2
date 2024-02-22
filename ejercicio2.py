

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
        

class Perro(Animal):
    def __init__(
            self,
            nombre: str,
            raza: str
            ):
        self.nombre=nombre
        self.raza=raza

    def correr(self):
        print("Estoy corriendo")

class Aguila(Animal):
    def __init__(self) -> None:
        pass
    def volar(self):
        print("Estoy volando")