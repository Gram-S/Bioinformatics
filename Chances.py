import random
import statistics

alphabet = ['a', 'c', 'g', 't']
target = random.choices(alphabet, k=9)
count = 1
counts = []

for i in range(1, 100):
    while True:
        if target == random.choices(alphabet, k=9):
            break
        else:
            count += 1
    counts.append(count)

print(counts)
print(statistics.mean(counts))