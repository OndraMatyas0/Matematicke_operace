
x = input("Zadejte proměnou x: ")
y = input("Zadejte proměnou y: ")
#Vklad uživatele, čeká než uživatel vloží číslo.
#čislo se poté uloží do x a y

x = int(x)
y = int(y)
#přepisujeme string na int


print(f"Proměná x = {x} a proměná y = {y}")
#vypíše proměnou zadanou uživatelem (f string)

print("---------------------------------------")
print(f"Příklad {x} + {y}")
print(f"Sčítání výsledek {x+y}")
print("---------------------------------------")
print(f"Příklad {x} - {y}")
print(f"Odčítání výsledek {x-y}")
print("---------------------------------------")
print(f"Příklad {x} * {y}")
print(f"Násobení výsledek {x*y}")
print("---------------------------------------")
print(f"Příklad {x} / {y}")
print(f"Dělení výsledek {x/y}")
#{x-y} stringy se nemůžou odčítat (lze opravit převodem str na int)
#Můžeme vylepšit přidáním pomlček


print("---------------------------------------")
print(f"Příklad {x} mocnina {y}")
print(f"mocnění výsledek {x**y}")
#levý alt + numerická klavesnice 9
# mocníme ** 
print("---------------------------------------")
print(f"Příklad {x} odmocnina {y}")
print(f"mocnění výsledek {x**(1/y)}")

#Zakladní matematická operace, nejdříve vydělíme a pak nasobíme