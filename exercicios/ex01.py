class Data:
    def __init__(self, dia:int, mes:int, ano:int ) -> None:
        self.dia = dia
        self.mes = mes
        self.ano = ano

    #dia
    def get_dia (self):
           return self.dia
    def set_dia (self, novo_dia):
        if 1 <= novo_dia <= 30:
            self.dia = novo_dia
        else:
            print("Dia invalido")

    #mes
    def get_mes (self):
        return self.mes    
     
    def set_mes (self, novo_mes):
        if 1 <= novo_mes <= 30:
            self.mes = novo_mes
        else:
            print("Mes invalido")

    #ano
    def get_ano (self):
        return self.ano  
    def set_ano (self, novo_ano):
        if novo_ano> 0:
            self.ano = novo_ano
        else:
            print("ano invalido")

    # representação em string legível de um objeto
    def __str__(self) -> str:
        return f"{self.dia}/{self.mes}/{self.ano}"
    
    # operação para avançar data para o dia seguinte 
    def proximoDia(self):
        if self.dia == 30 and self.mes == 12:
            self.ano += 1
            self.dia = 1
            self.mes = 1
        elif self.dia == 30:
            self.mes += 1
            self.dia = 1
        else:
            self.dia += 1

#a código de teste que instancie objetos 
d1 = Data(9, 3, 2002)

print("Data:", d1)

#modificando data
d1.set_dia(30)
d1.set_mes(12)
d1.set_ano(2057)

print(f"Data nova: {d1}")

d1.proximoDia()
#metodo proximo dia
print(f"Dia seguinte {d1}")