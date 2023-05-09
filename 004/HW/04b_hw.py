"""Napisz grę - kamień (k) / papier (p) / nożyce (n).

        Użytkownik podaje jedną z 3 figur.

        Komputer losuje jedną z 3 figur.

        Sprawdź kto wygrał tę rundę.

        Zmień kod tak, by użytkownik mógł podac liczbę rund.

        Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.

        Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’

"""
import random



# uin = int(input("pick your item (k,p,n):"))

items = ['k', 'p', 'n', 'koniec']
uin = input("pick your item (k,p,n):")
pcchoice = random.randint(0,2)
# print(pcchoice)
while uin not in items:
    uin = input("pick your item (k,p,n):")

uin = items.index(uin)
pcchoice = random.randint(0, 2)
res = pcchoice - uin
if res == 0:
    print(f"EVEN: RES = {res}, U: {items[uin]} vs PC:{items[pcchoice]}")
elif 0 > res or res == 2:
    print(f"USER WON! RES = {res}, U: {items[uin]} vs PC:{items[pcchoice]}")
elif 0 < res or res == -2:
    print(f"PC WON! RES = {res}, U: {items[uin]} vs PC:{items[pcchoice]}")

roundcnt = int(input("define rounds count:"))
rc = 0
uwins = 0
pcwins = 0
while rc <= roundcnt:
    while uin not in items[0:3]:
        uin = input("Pick your item (k,p,n):")

    uin = items.index(uin)
    pcchoice = random.randint(0, 2)
    res = pcchoice - uin
    if res == 0:
        print(f"ROUND #{rc}:  EVEN: U: {items[uin]} vs PC:{items[pcchoice]}")
    elif 0 > res or res == 2:
        print(f"ROUND #{rc}: USER WON! U: {items[uin]} vs PC:{items[pcchoice]}")
        uwins +=1
    elif 0 < res or res == -2:
        print(f"ROUND #{rc}: PC WON! RES = {res}, U: {items[uin]} vs PC:{items[pcchoice]}")
        pcwins += 1
    rc +=1

print(f"ROUNDS #{roundcnt}: PC {pcwins} vs USER {uwins}")

roundcnt = int(input("define rounds count:"))
rc = 0
uwins = 0
pcwins = 0
while rc <= roundcnt or uin == 3:
    while uin not in items:
        uin = input("PICK your item (k,p,n, koniec):")

    uin = items.index(uin)
    if uin == 3:
        break
    pcchoice = random.randint(0, 2)
    res = pcchoice - uin
    if res == 0:
        print(f"ROUND #{rc}:  EVEN: U: {items[uin]} vs PC:{items[pcchoice]}")
    elif 0 > res or res == 2:
        print(f"ROUND #{rc}: USER WON! U: {items[uin]} vs PC:{items[pcchoice]}")
        uwins +=1
    elif 0 < res or res == -2:
        print(f"ROUND #{rc}: PC WON! RES = {res}, U: {items[uin]} vs PC:{items[pcchoice]}")
        pcwins += 1
    rc +=1

print(f"ROUNDS #{rc}/{roundcnt}: PC {pcwins} vs USER {uwins}")
