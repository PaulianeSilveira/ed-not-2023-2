#Listas
# Listas são uma forma de armazenas mais de um valor em uma única variável.
# Os valores podem ser de tipos diferentes.
#Python: lista - JS: vetor ou array

#Uma lista de números
valores = [2,3,5,7,9,11]

#Uma lista com valores de tipos variados
mix = ["batata", 1.25, True, "tomate", 44]

#Lista de strings
legumes = ["batata", "tomate", "abobrinha", "cenoura"]

# Operações sobre listas

# 1) Percurso: percorrer a lista do 1º ao último elemento, fazendo algo com
#cada um deles.
#Imprimindo cada um dos elementos da lista, um por linha:
for val in valores:
    print(val)

print("-" * 40) # Traço de 40 hífens

#Imprimindo o dobro do valor de cada elemento da lista
for x in valores:
    print(x*2)
print("-" * 40) # Traço de 40 hífens

#2) INSERINDO UM NOVO ELEMENTO NO *FIM* DA LISTA

valores.append(13)
legumes.append("cebola")

print(valores)
print(legumes)

#3)INSERINDO UM NOVO ELEMENTO EM UMA POSIÇÃO ESPECÍFICA
#    Parâmetros:
#    1º: A posição onde será inserido o novo elemento 
#    2º o novo elemento a ser inserido

legumes.insert(2, "mandioquinha")
print(legumes)
legumes.insert(0, "beterraba")
print(legumes)

# valores .insert(30)
# print(valores)

print("-" * 40) # Traço de 40 hífens

#4)ACESSANDO UM VALOR EM POSIÇÃO ESPECÍFICA
print("Elemento na QUARTA posição:", valores [3])
print("Elemento na PRIMEIRA posição:", valores [0])
print("Elemento na ÚLTIMA posição:", valores [-1])
print("Elemento na PENÚLTIMA posição:", valores [-2])



