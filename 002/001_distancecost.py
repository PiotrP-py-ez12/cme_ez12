distance = 120
costpl = 5.04
usep100 = 6.4

total_cost = costpl* (distance*usep100)/100
print(f"Koszt przejechania 120km to: {total_cost}")


distance = input("Podaj dystans:")
print(f"Dystans: {distance}")
costpl = input("Cena paliwa PLN/l:")
print(f"Dystans: {costpl}")
usep100 = input("Zużycie paliwa na 100km:")
print(f"Dystans: {usep100}")

total_cost = costpl* (distance*usep100)/100
print(f"Dla podanych parametrów, koszt przejazdu wynosi: {total_cost} PLN")