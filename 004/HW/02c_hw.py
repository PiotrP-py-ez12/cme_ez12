"""Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych.
Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’)."""

# anyinput = 'sabrakadabra'
anyinput = input("Give me a string:")

print(f"Even pos by slice:{anyinput[1::2]}")
lst = []
for i in range(1,len(anyinput), 2):
    lst.append(anyinput[i])
print(f"Even by loop: {''.join(lst)}")
