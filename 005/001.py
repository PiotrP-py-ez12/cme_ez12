# Utwórz listę lists_to_dict zawierającą listy 2 elementowe. Przekształć ją w słownik dict_from_list.

# lists_to_dict = [['a',2], ['b',3], ['c',4], ['v',5]]
# dict_from_list = dict(lists_to_dict)
# for k in dict_from_list.keys():
#     print(dict_from_list[k])

#
# lst = [['*', '*','*','*'],['*', '*','*','*'],['*', '*','*','*'],['*', '*','*','*']]
# for n in lst:
#         r = ''
#         for l in n:
#             r += l+' '
#         print(r)
#
# c = '*'
# n = 4
# lst =[[c]*n]*n
#
# for r in lst:
#     print(' '.join(r))

# W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.
#
# """Szybko, zbudź się, szybko, wstawaj
# Szybko, szybko, stygnie kawa
# Szybko, zęby myj i ręce"""
#
# Zadbaj o sposób wyświetlania np.:
#
#     szybko : 5
#
#     zbudź : 1

# poem = """Szybko, zbudź się, szybko, wstawaj
# Szybko, szybko, stygnie kawa
# Szybko, zęby myj i ręce"""
#
# p1 = poem.strip().replace('\n',' ').replace(',','').lower().split(' ')
# print(p1)
# dct = {}
#
# dct ={}.fromkeys(p1)
# print(dct)
# for k in dct.keys():
#     dct[k] = p1.count(k)
# print(dct)
# for k in dct:
#     print(f"{k} count {dct[k]}")


# Usuń duplikat z podanej list i utwórzna jej bazie krotkę.Znajdź minimalną i maksymalną liczbę w krotce.

# example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]
# dct = {}.fromkeys(example_list)
# tpl = tuple(dct.keys())
# print(f"TUPLE: {tpl}, MAX.VAL: {max(tpl)}, MIN. VAL: {min(tpl)}")
# # TUPLE: (34, 17, 25, 41, 12, 194, 3, 99, 94), MAX.VAL: 194, MIN. VAL: 3

poem = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

poem_mod = poem.strip().replace('\n',' ').replace(',','').lower().split(' ')
print(poem_mod)
# work_dict = {}

work_dict ={}.fromkeys(poem_mod)
# print(work_dict)
for k in work_dict.keys():
    work_dict[k] = poem_mod.count(k)
# print(work_dict)
for k in work_dict:
    print(f"{k} : {work_dict[k]}")
    # print(f"{k} count {work_dict[k]}")

