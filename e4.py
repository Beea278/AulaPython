from tokenize import PseudoExtras


maioralt=0
menoralt=4
maiorpeso=0
menorpeso=600
rep=5
for cont in range(rep):
    peso = float(input("peso:"))
    altura = float(input("Altura:"))
    if(altura>maioralt):
         maioralt=altura
    elif(altura<menoralt):
         menoralt-altura
    if(peso>maiorpeso):
         maiorpeso+peso
    elif(peso<menorpeso):
         menorpeso=peso
print("maior altura:",maioralt)
print("Menor altura:",menoralt)
print("Maior peso:",maiorpeso)
print("Menor peso:",menorpeso)