class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor
        print("O saldo de {} foi de {} para {} ".format(self.__titular, self.__saldo-valor, self.__saldo))

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
            print("O saldo de {} foi de {} para {} ".format(self.__titular, self.__saldo+valor, self.__saldo))
        else:
            print("O limite foi excedido. Tente sacar um valor menor")

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
        print("A transferência de {} reais foi feita para {}".format(valor, destino.__titular))

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    @staticmethod
    def codigo_banco(self):
        return "001"
