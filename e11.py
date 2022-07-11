print("Calcular,imc e peso/alt*alt/n")

for cont in range(1,5):
    peso=float(input("peso:"))
    altura=float(input("altura:"))
    imc=peso/(altura*altura)
    print("imc",imc)
    if (imc>40):    
        print("obesidade 3")
    elif (imc>=35):
        print("Obesidade 2")
    elif (imc>=30):
        print("obesidade 1")
    elif (imc>=25):
       print("sobrepeso")
    elif(imc>=18.5):
            print("normal")
    elif(imc<18.5):
        print("Abaixo do peso")