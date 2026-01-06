from collections import Counter
import math

string = "TCGGGGGTTTTT CCGGTGACTTAC ACGGGGATTTTC TTGGGGACTTTT AAGGGGACTTCC TTGGGGACTTCC TCGGGGATTCAT TCGGGGATTCCT TAGGGGAACTAC TCGGGTATAACC"
temp = string.split(" ")
matrix = [list(item) for item in temp]
matrix = [list(row) for row in zip(*matrix)]

count_matrix = []
for i in matrix:
    count_matrix.append(Counter(i))

v = 0
for i in count_matrix:
    col = [i.get("A", 0), i.get("C", 0), i.get("G", 0), i.get("T", 0)]
    v2 = 0
    for j in col:
        log = math.log2(j/10) if j != 0 else 0 # 10 should be the number of rows in the original matrix
        v2 += (j/10) * log
    v += -1*v2
print(v)
    
