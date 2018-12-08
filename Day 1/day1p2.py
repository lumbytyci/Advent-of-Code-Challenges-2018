import itertools
data = [int(x) for x in open("input.txt").readlines()]

freq = 0
seen = {0}

for num in itertools.cycle(data):
    freq += num
    if freq in seen:
        print(freq); break
    seen.add(freq)
