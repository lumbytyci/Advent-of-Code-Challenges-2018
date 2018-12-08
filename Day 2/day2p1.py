data = [x.strip("\n") for x in open("input.txt").readlines()]
three_times = 0
two_times = 0

for line in data:
    seen = {0}
    for char in line:
        if line.count(char) == 2 and not (2 in seen):
            two_times += 1
            seen.add(2)
        elif line.count(char) == 3 and not (3 in seen):
            three_times += 1
            seen.add(3)

print("Two times: {}".format(two_times))
print("Three times: {}".format(three_times))

print("Checksum: {}".format(three_times * two_times))
