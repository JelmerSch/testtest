print("Je wil de juiste plek berijken, kies de juiste route!!\n"
      "Er zijn drie opties;")

#opties
eerste_keus = int(input(
    "1. Route B1 type 1\n"
    "2. Route B2 type 2\n"
    "3. Route B3 type 3"))

#keuzes
if eerste_keus == 1:
    print("Je hebt gekozen voor B1\n "
    "Er zijn twee nieuwe keuzes welke kies je")
    tweede_keus = int(input("1. kies voor B2 type 1\n"
                        "2. kies voor B3 type 2\n"))
    if tweede_keus == 1:
        print("Je hebt gekozen voor B2\n"
              "je kan doorgaan naar een nieuw niveau")
    elif tweede_keus == 2:
        print("Je hebt gekozen voor B3 dat is niet goed\n")

elif eerste_keus == 2:
    print("Je hebt gekozen voor B2\n"
          "Je kan doorgaan naar een nieuw niveau\n"
          "Hoera")

elif eerste_keus == 3:
    print("Je hebt gekozen voor B3\n"
          "Er zijn twee nieuwe keuzes welke kies je")
    tweede_keus = int(input("1. kies voor B1 type 1\n"
                        "2. kies voor B2 type 2\n"))
    if tweede_keus == 1:
        print("Je hebt gekozen voor B1\n"
              "dat is niet goed")
    elif tweede_keus == 2:
        print("Je hebt gekozen voor B2\n"
              "je kan doorgaan naar een nieuw niveau")

