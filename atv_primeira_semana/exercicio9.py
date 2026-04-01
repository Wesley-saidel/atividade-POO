class Usuario:
    primeiro_nome = ""
    sobrenome = ""
    def mensagem(self):
        return "ola"
usuario1 = Usuario()
usuario1.primeiro_nome = "Wesley"
usuario1.sobrenome = "Saidel"
print(usuario1.primeiro_nome)
print(usuario1.sobrenome)