class ContaCorrente:
    def __init__(self, numero:int, saldo:float) -> None:
        self.numero = numero
        self.__saldo = saldo #saldo privado
    
    def getSaldo(self): #metodo getter(para vizualizar)
        return self.__saldo
    
    def setSaldo(self,valor:float):#metodo setter(para vmodificar)
        self._saldo =valor
    
    def depositar(self, valor:float):
        if valor > 0:
            self.__saldo = self.__saldo + valor 
        else:
            print("Deposito apenas maiores que 0")

    def sacar(self, valor:float):
        if self.__saldo >= valor:
            self.__saldo = self.__saldo - valor
        else:
            print("Saldo insuficiente!")

c1 = ContaCorrente(12345, 1000)
c1.saldo = 1000000 #não vai funcionar 
print(f'Conta corrente numero {c1.numero},R$ {c1.getSaldo()}')
c1.depositar(900) 
print(f'Novo saldo: R${c1.getSaldo()}')
c1.sacar(500)
print(f'Novo saldo: R${c1.getSaldo()}')
