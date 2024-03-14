#login de 5 a 15
#no minimo 8 caracteres
class Cadastro:
    def __init__(self, login: str, senha: str) -> None:
        self.__login = login
        self.__senha = senha

        @property
        def login(self):
            return self.__login
        
        @login.setter
        def login(self, valor):
            l = len(valor)
            if l >= 5 and l <= 15:
                self.__login = valor
        
        @property
        def senha(self):
            return self.__senha
        
        @senha.setter
        def senha(self, senha):
            s = len(senha)
            if s >= 8:
                self.__senha = senha
            

c1 = Cadastro('rayaneferreira', '123456789')

print(c1.senha)
c1.senha = "1233456789"
