# day four 

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
        
print(len(set(passwords_updated)))