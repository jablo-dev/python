import math
print("Zadanie 1.")
b=int(input("Podaj liczbę: "))
a=int(4-b)/5
print(f"Wartość równania a = (4-b)/5 wynosi: {a}")

print("Zadanie 2.")
a=float(input("Podaj a: "))
b=float(input("Podaj b: "))
c=math.sqrt(a*b)
print(f"Średnia geometryczna tych dwóch liczb wynosi: {c}")

print("Zadanie 3.")
a=int(input("Podaj liczbę: "))
if a%2==0 and a==0 :
   print(f"Liczba {a} jest parzysta.")
else:
   print(f"Liczba {a} jest nieparzysta.")

