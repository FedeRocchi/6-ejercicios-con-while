print("---------------------------------")
print("AComplementario 6")
print("---------------------------------")


A1 = 1
A2 = 0

An = a1 + (2 * A2)

while (an<300) :
    A2 = A1
    a1 = an
    an = a1 + (2*A2)
    cont =  cont + 1

print("El rango es ", cont, "y el resultad es ", an)