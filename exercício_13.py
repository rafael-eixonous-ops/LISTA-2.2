# 13. O Problema do Número:  Tente executar este código:  idade = input("Sua idade: ")  . 
# Agora, tente somar  idade + 1  . Explique  por que o Python dará um erro se você não converter o dado. 

idade = int(input("Sua idade:"))

idade = idade + 1
print(idade)

# Imagine que o código funciona de dentro para fora:
# 1. input("Sua idade: ") roda primeiro e pega o texto "25".
# 2. O int(...) fica do lado de fora, pega esse texto "25" que o input acabou de receber e o transforma no número 25 de verdade.
# O int (abreviação de integer, que significa inteiro em inglês) é o tipo de dado que o Python usa para representar números inteiros.
# Números inteiros são aqueles que não possuem casas decimais (não têm ponto ou vírgula), podendo ser positivos ou negativos. Exemplos de int: 1, 5, 10, 100, -5.
# idade = (input("Sua idade:")) => ERRADO
