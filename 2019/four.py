# day four 
import re 

# part one 



passwords = []

for number in range(357253, 892942+1):
    for i in range(0,5):
        if (str(number)[i] == str(number)[i+1]):
            passwords.append(number)
    

passwords_updated = []
for number in passwords:
    if str(number)[5] >= str(number)[4] >= str(number)[3] >= str(number)[2] >= str(number)[1] >= str(number)[0]:
        passwords_updated.append(number)
        
print(f'Part one answer: {len(set(passwords_updated))}')


# part two 
part_two = []
for number in set(passwords_updated):
    score = 0 
    for i in range(4):
        if (str(number)[i] == str(number)[i+1]) and (str(number)[i] != str(number)[i+2]):
            score += 1 
    if score == 4 or score == 2 or score == 0:
        part_two.append(number)
            
            
print(len(part_two)) 

            