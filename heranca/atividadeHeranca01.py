class Usuario():
    def __init__(self,NomeUsuario=""):
        self.__NomeUsurio = NomeUsuario
    
    def SetNomeUsuario(self,NomeUsuario):
        self.__NomeUsurio = NomeUsuario
    
class admin(Usuario):
    def escrevaNome(self):
        return "admin"
    
    def digaOla(self):
        return "Olá admin,"+ self.NomeUsuario
    

admin1 = admin.SetNomeUsuario("baltazar")
print(admin1.digaOla)

