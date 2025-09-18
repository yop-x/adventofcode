# day two 

"""
1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99

"""

with open('./input_two.txt', 'r') as f:
    f = list(map(int, f.read().strip().split(',')))


def encode(numbers):
    
    for i in range(0, len(numbers), 4):
        op = numbers[i]
        if op == 99:
            break 
        
        
        first = numbers[i+1]
        second = numbers[i+2]
        result  = numbers[i+3]
        
        
        if op == 1:
            numbers[result] = numbers[first] + numbers[second]
    
            
        elif op == 2:
            numbers[result] = numbers[first] * numbers[second]
            
        else:
            raise ValueError(f'bad opcode {op} at postion {i}')
        
    return numbers 


            
for noun in range(0, 100):
    for verb in range(0,100):
        program = f[:]  # <- copy each time
        program[1] = noun
        program[2] = verb
        result = encode(program)
        if result[0] == 19690720:
            print("Found noun:", noun, "verb:", verb)
            print("Answer:", 100 * noun + verb)
            
