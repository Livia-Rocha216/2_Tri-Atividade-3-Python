# Exercício 2
palavra = input("Digite uma palavra. ")
n = 0

for letra in palavra:
    if letra in ["a","e","i","o","u","A","E","I","O","U"]:
        n += 1
    print("Palavra: "+palavra+"")
    print("Vogais:", n ,"")
