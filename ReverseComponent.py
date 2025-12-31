
pattern = "AAAACCCGGT"
reversecomponent = []

d = {
    'A':'T',
    'T':'A',
    'G':'C',
    'C':'G'
}
for i in pattern:
    reversecomponent.insert(0, d.get(i))

print(''.join(reversecomponent))
            