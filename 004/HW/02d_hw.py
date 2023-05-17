# 2▹ Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.

"""import random

n = 10
user_emulation = [random.randint(0,100) for _ in range(0,n)]
user_input = user_emulation"""

numbers_list = []
while len(numbers_list) <=10:
    user_inp = input("Give a number (0-100):")
    if user_inp.isdigit():
        numbers_list.append(int(user_inp))

        print(f"OK, is a number.  {10 - len(numbers_list)} to go. ")
user_input = numbers_list


print(user_input)
odd_numb = []
for number in user_input:
    if number%2 != 0:
        odd_numb.append(number)
print(f"Odd numbers: {odd_numb}")
