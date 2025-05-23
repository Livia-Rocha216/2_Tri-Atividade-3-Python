# Exercício 2
palavra = input("Digite uma palavra. ") # Pede ao usuário uma palavra.
n = 0 # Variável pra armazenar um valor temporário.

for letra in palavra: # Pra cada letra na palavra solicitada ao usuário...
    if letra in ["a","e","i","o","u","A","E","I","O","U"]: # O progrma verifica se existe alguma vogal;
        n += 1 # E o '+=' faz que ele avance verificando letra por letra.
    print("Palavra: "+palavra+"") # Este print mostra a palavra escrita pelo usuário;
    print("Vogais:", n ,"") # E este o número total de vogais.
