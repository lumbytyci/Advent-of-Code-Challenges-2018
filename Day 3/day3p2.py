import re
import numpy as np

data = [line.strip("\n") for line in open("input.txt").readlines()]
#1 @ 527,351: 24x10
#CLAIM_ID INCH_FROM_LEFT, INCH_FROM_TOP WxH

class Claim:
    def __init__(self, claim_id, inch_left, inch_top, width, height):
        self.claim_id = claim_id
        self.inch_left = inch_left
        self.inch_top = inch_top
        self.width = width
        self.height = height
        self.cords = self.calculate_coordinates()

    def calculate_coordinates(self):
        coords = []
        for i in range(0, self.width):
            for j in range(0, self.height):
                coords.append([self.inch_left + i, self.inch_top + j])
        return coords


regex_query = re.compile(r"^\#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)$")
claims = []
for line in data:
    tokens = regex_query.match(line)
    claims.append(Claim(tokens.group(1),int(tokens.group(2)), \
    int(tokens.group(3)),int(tokens.group(4)),int(tokens.group(5))))


overlapping_area = np.zeros((1000, 1000))

for claim in claims:
    for c in claim.cords:
        overlapping_area[c[0], c[1]] += 1


sum_area = overlapping_area >= 2

for claim in claims:
    area = 0
    for c in claim.cords:
        if sum_area[c[0], c[1]] == False:
            area += 1
        
    if area == (claim.width * claim.height):
        print(claim.claim_id); break