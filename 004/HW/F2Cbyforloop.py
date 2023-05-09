"""Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach.
Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.

    C = 5/9 * (F - 32) """
print("For loop presents:")
for i in range(0, 220, 20):
    print(f"{i}F -> {round(5/9*(i-32), 2)}C")

print("While loop presents:")
i= 0
while i <= 200:
    print(f"{i}F -> {round(5 / 9 * (i - 32), 2)}C")
    i+=20
