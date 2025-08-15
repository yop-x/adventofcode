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


print(checksum(lines))





# to find pair that with only one mismatch character at the same location 
