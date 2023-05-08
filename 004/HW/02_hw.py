"""Utwórz listę, która zawiera składniki na ulubione danie. Wyświetl komunikaty co należy pokolei dodać.
Poza pętlą umieść pozostałe instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”."""

tomyumlist = ['cebula', 'shitake', 'pasta tom yum', 'passata', 'mleczko kokosowe', 'tofu']

for n, ingr in enumerate(tomyumlist):
    print(f"#{n} dodaj: {ingr}")
print("Dodaj szczypiorek albo zjedz kimchi")