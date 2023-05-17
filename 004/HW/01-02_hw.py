# 1▹ Utwórz dowolną krotkę, w której elementy mogą się powtarzać. Przekształć ją w set.
# 2▹ Utwórz listę L_test = [1, 2, 3, 4], krotkę T_test = (1, 2, 3, 4) oraz set S_test = {1, 2, 3, 4}.
# Jakie metody dostępne dla typu list nie będą działać dla typów tuple i set?

sample = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
sample = tuple(sample.split())
print(sample)

sample_to_set = set(sample)
print(sample_to_set)

L_test = [1, 2, 3, 4]
T_test = (1, 2, 3, 4)
S_test = {1, 2, 3, 4}

L_test.append(T_test[0:3])
# L_test.append(S_test[0:3])
# T_test.append('append doesnt work for tuple and set')
# S_test.count('count doesnt work for set')
L_test.remove(2)
print(L_test)
# T_test.remove(2) all content modifiers doesn't work

