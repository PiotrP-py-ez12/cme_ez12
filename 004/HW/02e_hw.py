# 2▹ Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.

sample = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
sample = tuple(sample.split())
print(sample)
duplicates = []
for i in sample:

    c = sample.count(i)
    if c>1 and i not in duplicates:
        duplicates.append(i)
        print(f"Item '{i}' has duplicate ({c} occurence) in tuple")