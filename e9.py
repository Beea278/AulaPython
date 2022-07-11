print("numero positivo,negativo ou neutro")
for num in range(1,4):
    num = int(input("numero:"))
    if (num>0):
        print("positivo")
    elif (num<0):
        print("negativo")
    elif (num==0):
        print(num,"neutro")