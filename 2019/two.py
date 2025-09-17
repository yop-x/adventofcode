# day two 

"""
1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99

"""

with open('./input_two.txt', 'r') as f:
    f = list(map(int, f.read().strip().split(',')))


print(f) 

def encode(numbers):
    # numbers = numbers[:]  # uncomment if you don't want to mutate the input
    for i in range(0, len(numbers), 4):
        op = numbers[i]
        if op == 99:
            break  # halt
        
        a = numbers[i + 1]
        b = numbers[i + 2]
        dst = numbers[i + 3]

        if op == 1:
            numbers[dst] = numbers[a] + numbers[b]
        elif op == 2:
            numbers[dst] = numbers[a] * numbers[b]
        else:
            raise ValueError(f"Bad opcode {op} at position {i}")

    return numbers


print(encode(f))