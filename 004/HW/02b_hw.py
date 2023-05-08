"""Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5).
 Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie."""


secret_num = 5
uin=int(input("give a  number:"))
while uin != secret_num:
    uin = int(input("give a  number:"))
print("Match!")