
"""Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbwą.
Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
Połącz dane w jeden ciąg book za pomocą spacji
Policz liczbę wszystkich znaków w napisie book"""

title = input("Podaj tytul:")
author = input("Podaj autora:")
pagecnt = input("Podaj liczbe stron:")

# title = "lio grande"
# author = "Steinbeck"
# pagecnt = '44'

# 1Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbwą.
check1 = any(str.isdigit(char) for char in title)
check2 = any(str.isdigit(char) for char in author)
check3 = pagecnt.isnumeric()

print(f"Title contains digit? {check1}, Author name contains digit?: {check2}, Page count is a number? :{check3}")
# 2 Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
author = author[0].upper()+author[1:]
title = title[0].upper()+title[1:]
print(f"Author: {author}, Title: {title}")

# 3 Połącz dane w jeden ciąg book za pomocą spacji
book = ' '.join((title,author,pagecnt))
# 4 Policz liczbę wszystkich znaków w napisie book
print(f"Chars count in {book} is {len(book)}")
