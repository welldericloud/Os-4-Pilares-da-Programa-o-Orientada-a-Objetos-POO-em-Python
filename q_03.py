# 3. Crie três classes que herdam da classe Animal: 
# a. Cachorro 
# b. Gato 
# c. Pássaro 
# d. Cada uma deve aproveitar os atributos e o método 
# exibir_dados() da classe principal. 

# from q_02 import Animal  - Ia importar o metodo do outro arquivo...

class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_dados(self):
        print('Nome: ', self.nome, 'Idade: ', self.idade)

class Cachorro(Animal):
    def latir(self):
        pass

class Gato(Animal):
    def miar(self):
        pass

class Passaro(Animal):
    def piar(self):
        pass

cachorro = Cachorro('Rex', 5)
gato = Gato('Lian', 3)
passaro = Passaro('Chester', 2)

cachorro.exibir_dados()
gato.exibir_dados()
passaro.exibir_dados()