def analizuj_dane(lista_liczb, prog):
    wyniki = []  # Lista na wyniki
    for liczba in lista_liczb:
        if liczba > prog:
            wyniki.append(f"{liczba} jest większa niż próg")
        else:
            wyniki.append(f"{liczba} jest mniejsza lub równa progowi")
    return wyniki  # Funkcja zwraca wyniki

# Wywołanie funkcji
liczby = [1, 15, 8, 23, 5]
progi = 15
rezultat = analizuj_dane(liczby, progi)
for wiersz in rezultat:
    print(wiersz)
    
