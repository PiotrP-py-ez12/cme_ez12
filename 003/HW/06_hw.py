# Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl komunikat “gratulacje!”,
# w przeciwnym razie wyświetl “pudło!”.

hitnum = 44
usernum = float(input("Give a number between 0 and 100:"))
print(f"{'gratulacje!' if usernum == hitnum else 'pudło!'}")
