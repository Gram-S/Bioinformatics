

text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
d = 1

from collections import Counter

def hammingdist(string1, string2):
    hd = 0
    
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            hd += 1
    
    return hd

sub = [text[i:i+k] for i in range(len(text) - k + 1)]
freqmap = Counter(sub)
mismatchmap = Counter(sub)

for i in list(freqmap.keys()):
    for j in list(freqmap.keys()):
        hd = hammingdist(i,j)
        notsame = True if hd != 0 else False
        
        if notsame and hd <= d:
            mismatchmap[i] += freqmap[j]
        elif notsame and i == j[::-1]:
            mismatchmap[i] += freqmap[j]
            
print(freqmap)
print(mismatchmap)

m = max(mismatchmap.values())
mismatchmap = {u: v for u, v in mismatchmap.items() if v == m}

print(list(mismatchmap.keys()))