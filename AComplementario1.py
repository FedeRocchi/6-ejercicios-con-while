print("-------------------------------------")
print("Complementario 1")
print("-------------------------------------")


C = -1
I = 0
M = 0

while (C<O) or (I<=0) or (i>=100) or (m<=0) :

    print("introduce el capital, el interes y el tiempo apropiados")
    C = int(input("Capital :"))
    I = int(input("Interes :"))
    M = int(input("Tiempo en años :"))

for i in range(M):

    C = C*(1+I/100)

print("Tienes ",C, "soles")
