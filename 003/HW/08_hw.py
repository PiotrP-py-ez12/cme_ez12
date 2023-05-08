"""Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych. Znajdź największą liczbę.
Wyświetl liczby od największej do najmniejszej."""

num1 = 14
num2 = 121
num3 = 128

if num1 > num2:
    if num1 > num3:
        # print("num1 > nu2")
        if num2 > num3:
            print(num1, num2, num3)
        else:
            print(num1, num3, num2)
    else:
        print(num3, num1, num2)
elif num2 > num3:
    # print(num2)
    if num1 > num3:
        # print("num2 > nu3")
        print(num2,num1,num3)
    else:
        print(num2, num3, num1)
else:
    print(num3, num2, num1)


