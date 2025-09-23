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



def has_exact_doubles(s):
    i = 0 
    while i<6:
        j=i
        while j < 6 and s[j] == s[i]:
            j+=1
        if j - i ==2:
            return True
        
        i = j 
        
    return False 

part_two = [n for n in set(passwords_updated) if has_exact_doubles(str(n))]

print(len(part_two))