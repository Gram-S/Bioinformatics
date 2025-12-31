pattern = "CTTGATCAT"
genome = "AAGCATAAGCATAA"

with open('Vibrio_cholerae.txt', 'r') as file:
    genome = file.read()

answers = []
for i in range(len(genome) - len(pattern) + 1):
    if genome[i:i+len(pattern)] == pattern:
        answers.append(i)
        
print(answers)
    