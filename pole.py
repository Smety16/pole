predmety = ["Český jazyk", "Německý jazyk", "Počítačové sítě", "Aplikační software", "Hardware", "Tělocvik"]
print(len(predmety))
for i in predmety:
    print(i)
dalsiPredmet = input("Zadejte další přemět")
predmety.append(dalsiPredmet)
predmety.remove(3)
predmety.sort()
print(predmety.reverse())
