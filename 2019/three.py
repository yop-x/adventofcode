# day 3 

with open('./input_three.txt', 'r') as f:
    paths = f.read().strip().split('\n')

paths_a = paths[0].split(',')

paths_b = paths[1].split(',')


def give_coord(paths):
    coords = []
    x = 0 
    y = 0 
    
    for i in paths:
        if i[0] == 'R':
            for num in range(0, int(i[1:])):
                coords.append((x+1, y))
                x += 1
                
        elif i[0] == 'L':
            for num in range(0, int(i[1:])):
                coords.append((x-1, y))
                x -= 1 
        
        elif i[0] == 'U':
            for num in range(0, int(i[1:])):
                coords.append((x, y+1))
                y += 1 
                
        elif i[0] == 'D':
            for num in range(0, int(i[1:])):
                coords.append((x, y-1))
                y -= 1 
                
    return coords



print(len(give_coord(paths_b)), len(give_coord(paths_a)))



common = set(give_coord(paths_a)) & set(give_coord(paths_b))
            
print(f'the length of common coords is {len(common)}.') 


distances = [(abs(i[0])+abs(i[1])) for i in common]
print(min(distances))





str1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
str2 = 'U62,R66,U55,R34,D71,R55,D58,R83'
print(give_coord(str1.strip().split(',')))

common_part2_test = set(give_coord(str1.strip().split(','))) & set(give_coord(str2.strip().split(','))) 

print(f'the common coords for test 2 is {common_part2_test}.') 



nums = []
for coord in common:
    step_1 = (give_coord(paths_a)).index(coord) 
    step_2 = (give_coord(paths_b)).index(coord) 
    
    sum = step_1 + step_2 + 2 
    nums.append(sum)
    print(sum)
    
print(f'the part 2 minimum step is {min(nums)}.')
    

