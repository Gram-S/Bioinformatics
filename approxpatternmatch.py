def hammingdist(string1, string2):
    hd = 0
    
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            hd += 1
    
    return hd
        
text = "CGATCGAGTACCATAAG"
pattern = "ATA"
d = 1

k = len(pattern)
answers = []

for i in range(len(text) - k +1):
    if hammingdist(text[i:i+k], pattern) <= d:
       answers.append(i)

print(len(answers))

