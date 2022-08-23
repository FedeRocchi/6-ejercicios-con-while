print("----------------------------")
print("AComplementario 3")
print("----------------------------")


prim = -1
limite = 1000
cont = 0

for i =prim in range (limite) :

    primo = True
    j = 2

        while (i>j) and (primo == True) :

            if (i % j == 0) and (primo == True) :
            
                primo = False
                break
            else :
                j = j + 1

    if (primo == True) :

        print(i, "es primo")
        Cont = cont+1

print("Entre ", prim, " y ", limite, " hay ", cont, " n° primos")

