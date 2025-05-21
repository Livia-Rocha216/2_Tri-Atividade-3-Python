# Exercício 3 
numero1 = int(input("Digite um número. "))
numero2 = int(input("Digite mais um número. "))
numero3 = int(input("Digite um último número. "))
i = 0

numeros = [numero1,numero2,numero3]

while i < len(numeros):
    numeros[i] *= 2
    i += 1

print(numeros)
