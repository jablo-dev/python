print("Zadanie 1.")
i = 0
while i < 5:
   x = 3 ** i
   print(x)
   i = i+1

print(end = '\n')

print("Zadanie 2.")
i = 1
while i > 0:
   x = int(input("Podaj liczbę całkowitą: "))
   if x > 0:
      print(x)
   elif x <= 0:
      break
   else:
      print("Dziwna liczba.")

print(end = '\n')
    
print("Zadanie 3.")
suma = 0
while suma <= 100:
   x = int(input("Podaj liczbę całkowitą: "))
   if x % 2 == 0 and x >= 0: 
      suma = suma + x
   else:
      break
print(suma)
