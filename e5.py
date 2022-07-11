print ("verificar se ps numeros sao pares ou impares\n")
rep = 3
for cont in range(rep):
    numero = int(input("numero: "))
    if (numero%2) == 0:
        print ("par")
    else:
        print("impar")