# 2. Modifique a classe Animal para que: 
# a. O atributo idade seja definido como __idade. 
# b. Seja criado um método get_idade() para consultar a 
# idade. 
# c. Seja criado um método set_idade(nova_idade) que 
# permita alterar a idade somente quando o valor informado 
# for maior ou igual a zero. 

class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.__idade = idade

    def exibir_dados(self):
        print('Nome: ', animal.nome, 'Idade: ', animal.__idade)

    def emitir_som(self):
        print('O animal esta emitindo um som')

    def get_idade(self):
        print('Consulta idade: ', animal.__idade)

    def set_idade(self, nova_idade):
        if nova_idade >= 0:
            self.__idade = nova_idade
            animal.get_idade()
        else:
            print('Idade invalida! # Menor ou igual a zero #')



animal = Animal('Cachorro', 5)
animal.get_idade()
animal.exibir_dados()
animal.emitir_som()

new_idade = int(input('Informe uma idade: '))
animal.set_idade(new_idade)