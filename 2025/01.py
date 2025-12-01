

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

