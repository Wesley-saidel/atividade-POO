class Empregado:

    def __init__(self,nome="",salario="",projeto=""):
        self.__nome = nome
        self.__salario = salario
        self.__projeto = projeto


    def mostrar(self):
       return self.__salario , self.__nome
       

    def getTrabalho(self):
        return f"{self.__nome} trabalha no projeto {self.__projeto}"
    


guilherme = Empregado("guilherme",1500,"N/D")
print(guilherme.mostrar())
print(guilherme.getTrabalho())