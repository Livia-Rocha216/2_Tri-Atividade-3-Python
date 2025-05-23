# Exercício 3 
numero1 = int(input("Digite um número. ")) # Pede ao usuário o primeiro número;
numero2 = int(input("Digite mais um número. ")) # Pede ao usuário o segundo número;
numero3 = int(input("Digite um último número. ")) # Pede ao usuário o terceiro número.
i = 0 # Variável para armazenar um valor temporário.

numeros = [numero1,numero2,numero3] # Lista dos números armazenados.

print("Números:", numeros) # O primeiro print vai mostrar a lista de números sem nenhuma alteração.

def numeros_originais_soma(): # Essa função fará com que os números da lista sejam somados entre si.
    soma1 = sum(numeros)
    return soma1
print("Soma dos Números:", numeros_originais_soma()) # Print que mostra a soma da lista de números sem nenhuma alteração.

while i < len(numeros): # Enquanto a variável temporária 'i' tiver um valor abaixo da quantidade de itens da lista de números (3)...
    numeros[i] *= 2 # O 'i' assume a posição de cada número para multiplicar por 2;
    i += 1 # E o '+=' faz com que ele assuma a posição de todos os elementos da lista fazendo o 'while' acabar ao chegar no terceiro.

print("Números Multiplicados", numeros) # Este print mostra a lista com os números multiplicados pelo loop anterior.

def numeros_multiplicados_soma(): # Essa função faz com que a lista dos números multiplicados pelo loop anterior sejam somados entre si.
    soma2 = sum(numeros)
    return soma2
print("Soma dos Números Multiplicados:", numeros_multiplicados_soma()) # E o último print mostra a soma dos números que foram multiplicados anteriormente.

# :D