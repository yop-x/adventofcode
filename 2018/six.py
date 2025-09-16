with open('./input_six.txt', 'r') as f:
    lines = f.read().splitlines()
    

def manhattan(a, b):
    return sum(abs(x - y) for x, y in zip(a, b))

for line in lines:
    print(line)

coordinates = []
for i in range(-500, 501):
    for j in range(-500,501):
        coordinates.append([i, j])
        



diff = []
for coordinate in coordinates:
    distances = []
    for line in lines:
        
        print(line)
        distance = manhattan(line, coordinate)
        distances.append(distance)
    mindis = min(distances)
    
print(mindis)
