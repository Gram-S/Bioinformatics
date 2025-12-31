string1 = "GGGCCGTTGGT"
string2 = "GGACCGTTGAC"

hammingdist = 0

for i in range(len(string1)):
    if string1[i] != string2[i]:
        hammingdist += 1

print(hammingdist)