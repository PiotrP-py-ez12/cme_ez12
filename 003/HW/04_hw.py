"""Utwórz zmienną przechowującą dowolny ciąg znaków. Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis. """

# anyvar = 'sarutobiasume'
anyvar = input('give me some hash:')
print(f"String {anyvar} longer than 5 chars and contains 'a' char?: {'Yes' if len(anyvar) > 5 and anyvar.count('a') > 0 else 'NO'}")
if anyvar.count('a') > 0:
    anyvar = anyvar.replace('a', 'i')
    print(f"New and shiny 'anyvar': {anyvar}")