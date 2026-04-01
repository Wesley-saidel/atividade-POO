class pessoa:
    def __init__(self,nome,idade):
        self.__nome = nome
        self.__idade = idade

    
    def getNome(self):
        return self.__nome
    def getIdade(self):
          return self.__idade

class aluno(pessoa):
    def __init__(self, nome, idade, nota):
        super().__init__(nome, idade)
        self.__nota = nota

    def setNome(self,nome):
            self.__nome = nome

  
        
    def setIdade(self,idade):
            self.__idade = idade
        
   

    def setNota(self,nota):
            self.__nota = nota
        
    def getNota(self):
            return self.__nota
        
    def infoPessoa(self):
            return "eu sou"+self.getNome()+"e tenho"+self.getIdade()+"anos"
        
    def infoAluno(self):
            return f"sou o {self.getNome()} tirei {self.getNota()} e tenho {self.getIdade()}"
    

pessoa1 = pessoa("wesley",18)
aluno1 = aluno("wesley",18,10)
print(aluno1.infoAluno())