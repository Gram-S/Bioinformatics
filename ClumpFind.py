from collections import Counter

with open('E_coli.txt', 'r') as file:
    genome = file.read()
    
# From FrequentWords.py, takes in text and integer k and returns most frequent substrings of size k in text 
def FrequentWords(text, k, t):
    sub = [text[i:i+k] for i in range(len(text) - k + 1)]
    counted = Counter(sub)
    
    m = max(counted.values())
    key = [a for a, v in counted.items() if v == m and v >= t]
    return key

# genome = "ACGTACGT" 
k = 9   #k-mer (substring) size
L = 500 #Clump size (window)
t = 3   #Number of times a k-mer must appear to be added in the solution

answer = []
total = len(genome) - L +1
for i in range(len(genome) - L +1):
    Fw = FrequentWords(genome[i:i+L], k, t) #Added t to parameter to make it only return substrings larger than t as well
    answer += Fw 
    print(i, "out of ", total)
    
print(list(set(answer))) # Remove duplicates
print(len(list(set(answer)))) # Size
