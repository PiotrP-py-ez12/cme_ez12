"""Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę. Jeśli suma jest większa niż 100, wyświetl wynik,
w przeciwnym wypadku wyświetl “Koniec”."""

num1 = float(input("Give me a 1st number"))
num2 = float(input("Give me a 2nd number"))
numsum = num1+num2
print(f"RESULT: {numsum if numsum > 100 else 'Koniec'}")