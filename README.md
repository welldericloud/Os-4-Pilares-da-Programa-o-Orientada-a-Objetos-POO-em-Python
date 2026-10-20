# Os-4-Pilares-da-Programa-o-Orientada-a-Objetos-POO-em-Python
Entendendo os conceitos dos pilares da  orientação ao objeto(Abstração, encapsulamento,  polimorfismo e herança) 

7. Responda abaixo: 
a. Qual é a função da classe Animal no sistema? Como ela 
representa a abstração? 

R - A classe animal representa a abstração levando apenas caracteristicas gerais de um animal, não sendo 
caracteristicas individuais de cada um, sendo assim ela pode ser utilizada dentro de outras classes de animais
que são mais especificas individualmente
============================================================================================
b. Por que utilizamos __idade em vez de deixar o atributo 
totalmente acessível? 

R- Para que não seja tão facilmente acessada/alterada, somente por uma função pré-definida dentro da classe
============================================================================================
c. Qual é a vantagem de utilizar herança nas classes 
Cachorro, Gato e Passaro? 

R- Não precisar refazer sempre caracteristicas gerais/abstratas em todas as classes
============================================================================================
d. Por que o método emitir_som() apresenta resultados 
diferentes para cada animal? 

porque foi definida individualmente em cada classe
============================================================================================
e. O que aconteceria se tentássemos cadastrar um animal com 
idade negativa? Como o programa poderia impedir isso 
também no momento da criação do objeto? 

Com o IF utilizado ele simplesmente não atrubiu o novo valor a variavel.
Poderia criar um loop verificando se o valor informado é um inteiro maior que 0
