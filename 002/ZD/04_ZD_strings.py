# Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.
s1 = 'homo'
s2 = 'sapiens'

s3 = s1[:(len(s1)//2)+1]+s2
s3+=s1[(len(s1)//2):]
print(f"s1: {s1}, s2: {s2} {s3}")

"""
Do zmiennej quote przypisz zdanie:„Honesty is the first chapter in the book of wisdom.”,a następnie:
Policz wszystkie znaki w napisie
Nie modyfikując zmiennej wyświetl słowo wisdom
Wyświetl tylko pierwszą połowę tekstu
Wyświetl tylko kropkę 
Wyświetl od połowy tylko co trzecią literę cytatu
Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
Wyświetl cały cytat odwrotnie 
Zamień wisdom na słowo friendship
"""
quote = "Honesty is the first chapter in the book of wisdom."
print(f"Znakow: {len(quote)}")
print(f"1sthalf: {quote[:len(quote)//2]}")
print(f"dot: {quote[-1]}")
print(f"3rdchar: {quote[len(quote)//2::3]}")
print(f"3rdletter: {quote.replace(' ','')[len(quote)//2::3]}")
print(f"3rdletter: {quote[::2]}")
print(f"3rdletter: {quote[::-1]}")
print(f"3rdletter: {quote.replace('wisdom', 'friendship')}")
