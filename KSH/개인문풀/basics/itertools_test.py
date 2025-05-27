from itertools import permutations, combinations, product, combinations_with_replacement

data = ['A', 'B', 'C']

result1 = list(permutations(data, 2))
result2 = list(combinations(data, 3))
result3 = list(product(data, repeat=3))
result4 = list(combinations_with_replacement(data, 2))

print(result1, result2, result3, result4, sep="\n------\n")
