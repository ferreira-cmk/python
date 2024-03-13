

class Estudante:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.__idade = idade
# getter
    @property
    def idade(self):
       return self.__idade
       
# setter
    @idade.setter
    def idade(self, idade):
        if self.__idade <= 0:
            self.__idade 
        
                       
estudante = Estudante('Vanessa', 19)

print('Name:', estudante.nome, estudante.idade) # obtém idade usando getter
estudante.idade = -16 # altera idade usando setter (invocação setter)
print('Name:', estudante.nome, estudante.idade) # obtém idade usando getter