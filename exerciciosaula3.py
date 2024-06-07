# DESAFIO 01

# Crie um programa que leia o nome completo de uma pessoas
# e mostre

# O nome com todas as letras maiúsculas

# O nome com todas as letras minúsculas

# Quantas letras ao todo (sem considerar espaços)

# Quantas letras tem o primeiro nome

# nome=str(input("insira seu nome completo"))
# nomeMaiusculo=nome.upper()
# print(nomeMaiusculo)

# nomeMinusculo=nome.lower()
# print(nomeMaiusculo)

# semEspacotexto=nome.replace(" ","") 
# print(semEspacotexto)
# ContagemDeLetras=len(semEspacotexto)
# print(f"seu nome completo possui {ContagemDeLetras} letras sem considerar os espaços")
# dividefrase=nome.split()
# dividefrase2=dividefrase[0].upper()
# print(f"Seu primeiro nome é {dividefrase2}")


# DESAFIO 02

# Crie um programa que leia o nome de uma cidade e siga se ela
# começa ou não com o nome “Santo”.

# nomeCidade=str(input("insira o nome da cidade"))
# divideNomeCidade= nomeCidade.split()
# primeiroNomeCidade=divideNomeCidade[0].upper()
# verificaPalavraEmFrase="SANTO" in primeiroNomeCidade
# print(f"O nome da cidade {nomeCidade} começa com Santo: {verificaPalavraEmFrase}")




# DESAFIO 03

# Crie um programa que leia o nome de uma pessoa e diga se ela
# tem "Silva" no nome

# nome=(input("insira seu nome completo"))


# DESAFIO 04

# Faça um programa que leia uma frase pelo teclado e mostre:

# Quantas vezes aparece a letra "A"

# Em que posição ela aparece a primeira vez

# Em que posição ela aparece a ultima vez


# DESAFIO 05

# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o ultimo nome
# separadamente

# Exemplo: Ana Maria De Souza

# Primeiro: Ana

# Ultimo: Souza

# nomeCompleto = str(input("Digite seu nome: "))

# divideNome = nomeCompleto.split() #Inicia cada palavra dentro de um array
# tamanhoArray = len(divideNome)
# inicioNome = divideNome[0]
# fimNome = divideNome[tamanhoArray - 1]

# print(f"Primeiro Nome: {inicioNome}")
# print(f"Ultimo Nome: {fimNome}")
