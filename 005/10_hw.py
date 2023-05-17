"""10▹ Użytkownik podaje dowolną liczbę N. Napisz, który wygeneruje słownik, wg zasady,
że każdej liczbie przyporządkowany jest jej kwadrat (n : n * n).

Załóżmy, że użytkownik podał N = 8

Wynik: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}"""

# import random
#
# n = 7
# # sample = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
# user_emulation = random.randint(1,10)
# user_input = user_emulation

user_input = ''
while (not user_input.isdigit()) or (int(user_input) > 10):
    user_input = (input("Give some integer (1,10):"))


print(user_input)
sqrs_dict = {}
for i in range(1, int(user_input)+1):
    sqrs_dict[i] = i*i
print(sqrs_dict)
