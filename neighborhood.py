

text = "AAA"
alphabet = ['A', 'G', 'C', 'T']
n = 1 # Size of the mismatches allowed in the neighboorhood output set

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
print(list(set(neighborhood)))