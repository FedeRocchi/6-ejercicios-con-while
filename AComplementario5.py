from re import I


print("------------------------------------")
print("AComplementario 5")
print("------------------------------------")


print("Introduce un numero con valor X")
x = int(input("valor x:"))

e = 1
num = 1
den = 1
i = 1

num = x**i
den=den*i

i=i+1

e=e+num/den

while not (num/den<0.000001):
    num=x**i
    den=den*i
    i=i+1

    e=e+num/den


print("e elevado al ", x," es: ", e)