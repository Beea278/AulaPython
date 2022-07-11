print ("reajuste salarial")
salario = float(input("salario:"))
if (salario>1000):
    salnovo  =  salario+(salario*0,00)
elif(salario>500):
    salnovo = salario+(salario*0,10)
elif(salario>500):
    salnovo = salario+(salario*0,15)
print ("Salario novo:",salnovo)