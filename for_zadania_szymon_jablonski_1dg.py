print("Zadanie 1a.")
for i in range(3,27,4):
    print(i, end=' ')

print(end='\n')

print("Zadania 1b.")
for i in range(9,4,-1):
    print(i, end=' ')

print(end='\n')

print("Zadanie 2.")
liczba=int(input("Podaj liczbę: "))

silnia=1
if liczba < 0:
   print("Silnia dla liczb ujemnych nie istnieje.")
elif liczba == 0:
   print("0! = 1")
else:
   for i in range(1,liczba+1):
      silnia=silnia*i
   print(f"{liczba}! = {silnia}")

