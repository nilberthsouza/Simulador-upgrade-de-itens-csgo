import random

nome_item = input("Digite o nome do item que você quer apostar: ")
valor_item = float(input("Digite o valor do item que você quer apostar: "))
valor_vencer = float(input("Digite o valor do item que você quer vencer: "))

razao = valor_item / valor_vencer
probabilidade = razao

if probabilidade > 1:
    probabilidade = 1
    
probabilidade_casa = probabilidade * 0.9

ganhou = random.random() < probabilidade
if ganhou:
    print(f"Você ganhou! Parabéns, você ganhou um {nome_item}.")
else:
    print(f"Você perdeu! Infelizmente, você perdeu seu {nome_item}.")

