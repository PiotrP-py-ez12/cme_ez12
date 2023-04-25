w=80
h=1.8

bmi=w/(h**2)
print(f"BMI : {bmi}")
w = input("Twoja kolej, podaj wage i wzrost:")
h = input("podaj wzrost:")
w=float(w)
h=float(h)
bmi=w/(h**2)
print(f"Twoje BMI{bmi}")

print(f"Twoje okragle BMI{round(bmi,2)}")
