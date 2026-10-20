# 4. Sobrescreva o método emitir_som() em cada classe para 
# apresentar as seguintes mensagens:  
# a. Cachorro = “Au au”(mensagem que deverá ser 
# implementada) 
# b. Gato = x (mensagem que deverá ser implementada) 
# c. Louro = y (mensagem que deverá ser implementada) 

class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_dados(self):
        print('Nome: ', self.nome, 'Idade: ', self.idade)

class Cachorro(Animal):
    def emitir_som(self):
        print('Au Au')



class Gato(Animal):
    def emitir_som(self):
        print('Miau miau')

class Passaro(Animal):
    def emitir_som(self):
        print('Pru Pru')

cachorro = Cachorro('Cachorro', 5)
gato = Gato('Gato', 3)
passaro = Passaro('Louro', 2)

# cachorro.exibir_dados()
# gato.exibir_dados()
# passaro.exibir_dados()

animais = [Cachorro('Cachorro', 9), Gato('Gato', 7), Passaro('Louro', 5)]

for animal in animais:
    animal.emitir_som()