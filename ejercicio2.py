

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
            cantidad_patas: int,
            tipo: str,
            nombre: str,
            raza: str
            ):
        self.nombre=nombre
        self.raza=raza
        super().__init__(cantidad_patas, tipo)
    def correr(self):
        print("Estoy corriendo")


class Aguila(Animal):
    def __init__(
            cantidad_patas: int,
            tipo: str,
            self
            ):
        super().__init__(cantidad_patas, tipo)
    def volar(self):
        print("Estoy volando")