genome = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"

d = {
    'G':1,
    'C':-1
}

skew = [0]
index = 0

for i in genome:
    skew.append(skew[index] + d.get(i, 0))
    index += 1
    
minimum = min(skew)
indices = [j for j, v in enumerate(skew) if v == minimum]

print(skew)
print(indices)