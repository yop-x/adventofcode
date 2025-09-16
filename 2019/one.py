with open("./input_one.txt", "r") as f:
    lines = f.readlines()
    
    



modules = []
for line in lines:
    modules.append(line)
    
    
results = [int(float(int(number)/3))-2 for number in modules]

final = 0 
for number in results:
    final += number 
    
    
print(final)
    