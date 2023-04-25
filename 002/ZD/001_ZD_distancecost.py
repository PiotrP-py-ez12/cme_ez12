
distance = float(input("Podaj dystans:").replace(',', '.'))
print(f"Dystans: {distance}")
costpl = float(input("Cena paliwa PLN/l:").replace(',', '.'))
print(f"Cena: {costpl}")
usep100 = float(input("Zużycie paliwa na 100km:").replace(',', '.'))
print(f"Zużycie: {usep100}")

total_cost = costpl* (distance*usep100)/100
print(f"Dla podanych parametrów, koszt przejazdu wynosi: {round(total_cost, 2)} PLN")