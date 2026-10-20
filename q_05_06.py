# 5. No programa principal, crie os seguintes objetos:
# cachorro = Cachorro('Rex', 3)
# gato = Gato('Mimi', 2)
# passaro = Passaro('Louro', 1)

# 6. Em seguida, coloque os objetos em uma lista e utilize um laço for 
# para chamar os métodos exibir_dados() e emitir_som() de 
# cada animal. 


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

cachorro = Cachorro('Rex', 3)
gato = Gato('Mimi', 2)
passaro = Passaro('Louro', 1)

# cachorro.exibir_dados()
# gato.exibir_dados()
# passaro.exibir_dados()

animais = [cachorro, gato, passaro]

for animal in animais:
    animal.exibir_dados()
    animal.emitir_som()