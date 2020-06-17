conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}

conjunto_uniao = conjunto.union(conjunto2)
print('União: {}'.format(conjunto_uniao))

conjunto_intersecao = conjunto.intersection(conjunto2)
print('Interseção: {}'.format(conjunto_intersecao))

conjunto_diferenca = conjunto.difference(conjunto2)
print('Diferênça entre c1 e c2: {}'.format(conjunto_diferenca))

conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferênça entre c2 e c1: {}'.format(conjunto_diferenca2))

conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferênça simétrica: {}'.format(conjunto_diff_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}

print(conjunto_a)
print(conjunto_b)

conjunto_subset = conjunto_a.issubset(conjunto_b)
print('Conjunto a está contido no conjunto b? {}'.format(conjunto_subset))

conjunto_subset = conjunto_b.issubset(conjunto_a)
print('Conjunto b está contido no conjunto a? {}'.format(conjunto_subset))

conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('Conjunto b é um superconjunto de a? {}'.format(conjunto_superset))

conjunto_superset = conjunto_a.issuperset(conjunto_b)
print('Conjunto a é um superconjunto de b? {}'.format(conjunto_superset))

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print('Lista: {}'.format(lista))
print(lista)

conjunto_animais = set(lista)
print('Conjunto animais: {}'.format(conjunto_animais))
print(conjunto_animais)

lista_animais = list(conjunto_animais)
print('Lista animais: {}'.format(lista_animais))
print(lista_animais)


# conjunto = {1, 2, 3, 4, 4, 2}
# print(type(conjunto))
#
# conjunto.add(5)
# conjunto.discard(2)
#
# print(conjunto)
