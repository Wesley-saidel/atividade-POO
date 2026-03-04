class Robo():
    def __init__(self,nome,ano_construcao):
        self.__nome = nome
        self.__ano_construcao = ano_construcao
    
    def getNome(self):
        return self.__nome
    
    def getAno(self):
        return self.__ano_construcao
    
    def setNome(self,nome):
        self.__nome = nome

    def setAno(self,ano_construcao):
        self.__ano_construcao = ano_construcao
    
        
        

    def diga_alo(self,):
        return f"Eu sou o {self.__nome} e fui construido em {self.__ano_construcao}"

Robo1 = Robo("clebinho",1999)
print(Robo1.diga_alo())