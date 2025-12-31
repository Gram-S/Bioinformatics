from collections import Counter

text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4

sub = [text[i:i+k] for i in range(len(text) - k + 1)]
counted = Counter(sub)

m = max(counted.values())
key = [a for a, v in counted.items() if v == m]

print(key)