#While_1

#input 

print("╔═══════════════════════════╗")
n = int(input("Digite su Numero: "))
print("╚═══════════════════════════╝")

#proccesing

S = 0
I = 1

while I<=n:
    S = S+I
    I = I+1

# Output

print("╔══════════════════════════════════════════════════╗")
print("La suma de los primeros "+ str(n)+" es: "+str(S))
print("╚══════════════════════════════════════════════════╝")
