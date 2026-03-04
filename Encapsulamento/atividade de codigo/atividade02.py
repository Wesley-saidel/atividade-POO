class Usuario:
    def __init__(self,primeironome):
        self.__primeironome = primeironome


    def getPrimeironome(self):
        return self.__primeironome

    
usuario1 = Usuario("JOE")
print(usuario1.getPrimeironome())