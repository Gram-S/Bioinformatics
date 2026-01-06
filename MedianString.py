k = 3
dna = "AAATTGACGCAT GACGACCACGTT CGTCAGCGCCTG GCTGAGCACCGG AGTACGGGACAG"
dna = dna.split(" ")

from itertools import product 

def hammingdist(string1, string2):
    hd = 0
    
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            hd += 1
    
    return hd

def d(Pattern, List, k):
    sum = 0
    for string in List: 
        
        # Find the kmer with smallest hamming distance from pattern in string
        kmers = [string[i:i+k] for i in range(len(string) - k + 1)]
        min_kmer = None
        current = float('inf')
        
        # Find kmer with the smallest hamming dist to the pattern
        for kmer in kmers:
            dist = hammingdist(Pattern, kmer)
            if current >= dist:
                current = dist
                min_kmer = kmer
                
        # print(min_kmer, hammingdist(Pattern, min_kmer)) # DEBUG
        sum += hammingdist(Pattern, min_kmer)
    return sum 
                

def median_string(dna: list[str], k: int) -> str:
    dist = float('inf')
    Median = ""
    
    # Generate every possible kmer? 
    alphabet = ['A','G','C','T'] 
    permutations = product(alphabet, repeat=k) # generate combinations with replacement and wher order matters
    allkmers = [''.join(item) for item in permutations] # combine them as a string
    
    for kmer in allkmers:
        hamming_sum = d(kmer, dna, k)
        # print(kmer, hamming_sum) # DEBUG
        if dist > hamming_sum:
            dist = hamming_sum
            Median = kmer
        
    return Median
    
    
print(median_string(dna, k)) # I dont know why there is an error here when it runs fine