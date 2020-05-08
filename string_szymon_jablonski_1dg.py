print("Zadanie 1.")
aaa = input("Podaj imię: ")
print(aaa.lower())
print(aaa.upper())
print(aaa.capitalize())

print("Zadanie 2.")
bbb = aaa.endswith('a')
if bbb == True or aaa.lower() == "beatrycze":
   print(f"Szanowna Pani")
else:
   print("Szanowny Panie")

print("Zadanie 3.")
ccc = input("Podaj jakieś słowo, a dostaniesz palindrom: ")
print(f"{ccc}{ccc[::-1]}")