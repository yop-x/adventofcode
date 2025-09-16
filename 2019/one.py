with open("./input_one.txt", "r") as f:
    lines = f.readlines()
    

# Part 1 



modules = []
for line in lines:
    modules.append(line)
    



def get_fuel(number):
    fuel = int(number)//3 - 2 
    return fuel
    
    
    
    
final = 0 
for number in modules:
    final += get_fuel(number)
    
    
print(f'The answer to part one is {final}.')
    
    

# Part 2 
"""

A module of mass 14 requires 2 fuel. 
This fuel requires no further fuel (2 divided by 3 and rounded down is 0, which would call for a negative fuel), 
so the total fuel required is still just 2.

At first, a module of mass 1969 requires 654 fuel. 
Then, this fuel requires 216 more fuel (654 / 3 - 2). 
216 then requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, which requires no further fuel. 
So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
The fuel required by a module of mass 100756 and its fuel is: 
33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346. 
"""


#take one number and return the total sum 


1969 



def recursive_fuel(number):
    
    new_number = get_fuel(int(number))
    
    
    if new_number <= 0:
        return 0 
        
    else:
        return new_number + recursive_fuel(new_number)
    


final = 0 
for num in modules:
    final += recursive_fuel(num)
    
print(f'the answer to part two is {final}.')