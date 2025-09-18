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
