# parse the input
with open('day1.input', 'r') as file:
    pairs = [l.split('   ') for l in file.readlines()]
    
A, B = [int(pair[0]) for pair in pairs], [int(pair[1]) for pair in pairs]

# part 1
print(f'part one: {sum([abs(a - b) for (a, b) in zip(sorted(A), sorted(B))])}')

# part 2
print(f'part two: {sum([a * sum([1 if a == b else 0 for b in B]) for a in A])}')
