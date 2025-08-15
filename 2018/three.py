#2018
#03 

#part 1 

#1 @ 49,222: 19x20
#2 @ 162,876: 28x29
#3 @ 28,156: 17x18
#4 @ 673,337: 24x24
#5 @ 213,834: 20x23
#6 @ 675,523: 20x13
from collections import defaultdict


with open("./input_three.txt", "r") as f:
    lines = []
    for i in f.readlines():
        lines.append(i[:-1])
    

def parse(claim):
    claim = claim.strip().split(' ')
    claim_number = claim[0][1:]
    left, top = claim[2][:-1].split(',')
    width, height = claim[-1].split('x')
    return claim_number, left, top, width, height


print(parse(lines[-2]))

def overlap(claims):
    claims_list = []
    for claim in claims:
        claims_list.append(parse(claim))
    
    
    counts = defaultdict(int)
    

    for id_str, left_str, top_str, width_str, height_str in claims_list:
        claim_id = int(id_str)
        left, top, width, height = map(int, (left_str, top_str, width_str, height_str))
        for x in range(left, left + width):
            for y in range(top, top+height):
                counts[(x,y)] += 1
                
    values = 0 
    for i in counts.values():
        if i >= 2:
            values += 1
            
    return values
            
print(overlap(lines))