# 1. Crie uma classe chamada Animal que possua: 
# a. Os atributos nome e idade. 
# b. Um método chamado exibir_dados(), que apresente o 
# nome e a idade do animal. 
# c. Um método chamado emitir_som(), que inicialmente 
# apresente a mensagem "O animal está emitindo um 
# som". 

class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_dados(self):
        print('Nome: ', animal.nome, 'Idade: ', animal.idade)

    def emitir_som(self):
        print('O animal esta emitindo um som')

animal = Animal('Cachorro', 5)
animal.exibir_dados()
animal.emitir_som()

