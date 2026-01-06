DNA = "ACGT ACGT ACGT"
k = 3
d = 0

def neighborhood(text, alphabet, n):
    neighborhood = [text]
    
    while n > 0:
        templist = []
        for x in neighborhood:
            for i in range(len(x)):
                for j in alphabet:
                    xtext = list(x)
                    xtext[i] = j
                    templist.append("".join(xtext))
        
        neighborhood += templist
        n-=1   
    return list(set(neighborhood))  

dlist = DNA.split(" ")
dneighborhood = []

for idna in dlist:
    kmers = [idna[i:i+k] for i in range(len(idna) - k + 1)]
    fullneighborhood = []
    for j in kmers:
        fullneighborhood += neighborhood(j, ['A','G','C','T'], d)
    dneighborhood.append(fullneighborhood)
        
intersection_set = set.intersection(*map(set, dneighborhood))
print(list(intersection_set))

    
        
