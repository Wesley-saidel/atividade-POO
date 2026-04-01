class Usuario:
    primeiro_nome = ""
    sobrenome = ""
    def mensagem(self):
        return f"Olá {self.primeiro_nome} {self.sobrenome}"
usuario2 = Usuario()
usuario2.primeiro_nome = "Jane"
usuario2.sobrenome = "Silva"
print(usuario2.mensagem())