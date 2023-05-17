# 4▹ Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.
# import random
#
# n = 7
# sample = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
# user_emulation = [random.randint(0,100) for _ in range(0,n)]
# user_input = user_emulation
# sample = sample.split()
# user_input = [random.choice(sample) for _ in range(1,21)]

user_input = []
c = ''
while c != 'q':
    c = input("Give me some input ('q' for end)")
    user_input.append(c)


print(user_input, type(user_input))
lngh = len(user_input)
if lngh%2 == 0:
    item1 = user_input[int(len(user_input)/2)-1]
    item2 = user_input[int(len(user_input)/2)]
    print(user_input[int(len(user_input)/2)-1:int(len(user_input)/2)+1])
    print(f"Items {item1} and {item2} equal?: {'YES' if item1 == item2 else 'NO'}")
else:
    print(f"Received odd count of input items {len(user_input)}")
