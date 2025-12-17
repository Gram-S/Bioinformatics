from re import Pattern


text = "AGCTTAGGCTAGCTACATGCATGCATGACTAGGAGCATAGATTACAT"
pattern = "CAT" 

count = 0

for i in range(0, len(text) - len(pattern)+1):
    if text[i:i+len(pattern)] == pattern:
        count += 1
    