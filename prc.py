#1
n = int( input("Zadejte číslo, jehož dělitelé mají být vypsáni: ") )
for k in range(1, n+1):
 if n % k == 0:
 print(k, end=" ")

#2
def PrvociselnyRozklad(n):
    print("{} - rozklad na prvočísla:\t".format(n), end="")
    i = 2
    while n > 1:
        if n % i == 0:
            print(i, end=" ")
            n = n // i
        else:
         i = i + 1
 print()


k = int(input("Zadejte číslo, jež rozložíme na prvočísla: "))
PrvociselnyRozklad(k)

#3
def faktorial_for(n):
    f = 1
    for i in range(1, n+1):
         f = f * i
    return f

#4
N = 5 
for u in range(1, N+1):
    for v in range(1, u):
        print("{}\t{}\t{}".format(u*u - v*v, 2*u*v,))