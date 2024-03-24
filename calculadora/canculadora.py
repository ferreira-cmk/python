
class calculadoraDaRay:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
        pass

    def somar(self):
        return self.a + self.b
    
    def multi (self):
        return self.a * self.b
    
    def subt (self):
        return self.a - self.b
    
    def div (self):
        return self.a / self.b


calcular = calculadoraDaRay(10,10) #exemplo de entrada

print("A soma dos numero é:", calcular.somar() )
print("A multiplicação dos numero é:", calcular.multi() )
print("A subtração dos numero é:", calcular.subt() )
print("A divisão dos numero é:", calcular.div() )

