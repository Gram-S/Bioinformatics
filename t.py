import itertools
k = 3

alphabet = ['A','G','C','T']
n = 4
permutations = itertools.product(alphabet, repeat=k)

allkmers = [''.join(item) for item in permutations]
print(allkmers)