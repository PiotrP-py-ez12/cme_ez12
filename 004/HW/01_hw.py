'''▹ Stwórz krotkę zawierającą dane twojego pupila (rodzaj zwierzecia, rasa, jak się wabi). Następnie rozpakuj tę krotkę na pojedyńcze zmienne.
Wykorzystaj zmienne do wyświetlenia f-stringa, tak by mogło powstać zdanie np. “Mój pies, rasy border collie wabi się Dyzio”'''

data = ('Yeti', 'Yeti nizinne', 'Chewbacca')

species, race, name = data
print(f"Moj {species} rasy {race} wabi sie {name}. ")