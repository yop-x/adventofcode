#advent of code 
#2018
#01 

def calculate(lines):
    result = 0 
    for command in lines:
        command = command.strip()
        if command:
            result += int(command)  
    return result 


with open("./input_one.txt", "r") as f:
    lines = f.readlines()
    
print("resulting freq: ", calculate(lines))


def calculate_two(lines):
    result_freq = {0}
    freq = 0
    while True:   
        for command in lines:
            command = command.strip()
            if command:
                freq += int(command)
                if freq in result_freq:
                    print(freq)
                    return freq
                else:
                    result_freq.add(freq)


print("resulting freq: ", calculate_two(lines))

