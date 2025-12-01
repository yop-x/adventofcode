

# part one 
with open("./input_01.txt", 'r') as f:
    x = f.read().strip().split('\n')
    
    
code = 50 

real_code = 0 


for step in x:
    if step[0] == 'L':
        code = code - int(step[1:]) 
        code = code % 100 
        if code < 0: 
            code = 100 - abs(code)
            
        elif code == 0:
            real_code += 1 
        
    elif step[0] == 'R':
        code = code + int(step[1:]) 
        code = code % 100 
        if code == 0:
            real_code += 1
        elif code < 0:
            code = 100 - abs(code)
        
        
print(f"The answer for part one is {real_code}.")


# part two 
code = 50 
real_code = 0 
# x = ['L68',
#     'L30',
#     'R48',
#     'L5',
#     'R60',
#     'L55',
#     'L1',
#     'L99',
#     'R14',
#     'L82']

for step in x:
    if step[0] == 'L':
        
        code = code - int(step[1:])
        if code < 0 and (abs(code) // 100 == 0):
            real_code += 1 
            
        q = abs(code) // 100 
        real_code = real_code + q 
        
        code = code % 100
        
        if code < 0: 
            code = 100 - abs(code)
            
            
        elif code == 0:
            code = code
            real_code += 1 
            
            
    if step[0] == 'R': 
        code = code + int(step[1:])
        if code > 99 and (abs(code) // 100 == 0):
            real_code += 1 
            
        q = abs(code) // 100 
        real_code = real_code + q 
        code = code % 100


        if code < 0:
            code = 100 - abs(code)
            
            
            
        elif code == 0:           
            real_code += 1 

        
            
print(f"The answer for part two is {real_code}")

