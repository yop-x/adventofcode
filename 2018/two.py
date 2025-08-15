#advent of code 
#2018 
#02

from collections import Counter 

with open("./input_two.txt", 'r') as f:
    lines = f.readlines()




def checksum(lines):
    if lines is None:
        raise ValueError('Input is invalid.')
    
    count_2 = 0 
    count_3 = 0 
    
    
    
    for line in lines:
        line = line.strip()
        freq = Counter(line)
        if 2 in freq.values():
            count_2 += 1 
            
        if 3 in freq.values():
            count_3 += 1
            

    return count_2 * count_3


print("the result of part one: ", checksum(lines))




# abcde
# fghij
# klmno
# pqrst
# fguij
# axcye
# wvxyz 


def mismatch_by_one(a, b):
    if len(a) != len(b):
        return False
    
    
    mismatch_count = 0
    
    for i in range(len(a)):
        if a[i] != b[i]:
            mismatch_count += 1
            if mismatch_count > 1:
                return False
    
    if mismatch_count == 1:
        return True

def check_pair(lines):
    
    pair_list =  []
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            if mismatch_by_one(lines[i], lines[j]):
                pair_list.append((lines[i], lines[j]))
             
            
    return pair_list






# to find pair that with only one mismatch character at the same location 
print("part two: ", check_pair(lines))