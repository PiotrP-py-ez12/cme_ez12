"""Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N (N podane przez użytkownika, ale nie większe niż 8)."""
n = 1
nn =[]
userin = int(input("Give a number < 8:"))
if userin < 8 and userin != 0:
    for l in range(1,userin+1):
        n = n*l
        nn.append(str(l))
        print(f"NI: {l} {n}")
elif userin > 8:
    print("Nie robie...")

print(f"Silnia {userin}: {userin}! = {'*'.join(nn)} = {n}")


