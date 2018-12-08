data = [x.strip("\n") for x in open("input.txt").readlines()]



def diff_letters(a,b):
    return sum (a[i] != b[i] for i in range(len(a)))

def compare_lines(line1, startIndex, data):
    for i in range(startIndex + 1, len(data)):
        line2 = data[i]
        if(diff_letters(line1, line2) == 1):
            return True
    return False

for index,line in enumerate(data):
    found = compare_lines(line, index, data)
    if found: break

print(line)