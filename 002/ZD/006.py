
"""X
    Przekopiuj zawartość import this do zmiennej.

import this

    Policz liczbę wystąpień słowa better.

    Usuń z tekstu symbol gwiazdki

    Zamień jedno wystąpienie explain na understand

    Usuń spacje i połącz wszystkie słowa myślnikiem

    Podziel tekst na osobne zdania za pomocą kropki"""

import this

# s = "".join([this.d.get(c, c) for c in this.s])
# print(s)

pyzen = """The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

# 1 Policz liczbę wystąpień słowa better.

bcnt = pyzen.count('better')
# print(f"'better' count: {bcnt}")
# 2 Usuń z tekstu symbol gwiazdki
pyzen = pyzen.replace('*', '')
# print(pyzen)
# 3 Zamień jedno wystąpienie explain na understand

print(f"'explain' count: {pyzen.count('explain')}")
pyzen = pyzen.replace('explain', 'understand', 1)
# print(f"'explain' count after replace: {pyzen.count('explain')}")
print(pyzen)
#4 Usuń spacje i połącz wszystkie słowa myślnikiem
pyzen = pyzen.replace(' ', '-')
pyzen = pyzen.replace('--', '-')
pyzen = pyzen.replace('--', '-')
print(pyzen)
# 5Podziel tekst na osobne zdania za pomocą kropki

sep_sent = pyzen.split('.')
for sent in sep_sent:
    print(sent)