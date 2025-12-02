# part one 

with open('./input_01.txt', 'r') as f:
    x = f.read().strip('./').split()
    

code = 50 
real_code = 0 


# x = ['L68',
#      'L30',
#      'R48',
#      'L5',
#      'R60',
#      'L55',
#      'L1',
#      'L99',
#      'R14',
#      'L82']




for step in x:
    direction = step[0]
    distance = int(step[1:]) 
    
    if direction == 'L':
        code = (code - distance) % 100 
        
    elif direction == 'R':
        code = (code + distance) % 100 
        
    if code == 0: 
        real_code += 1 
        
        
        
print(f'part one: {real_code}')
        
    