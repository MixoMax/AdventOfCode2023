#Advent of Code 2023 Day 1 Part 1

with open("data.txt", "r") as f:
    input_lines = f.readlines()

s = 0
for line in input_lines:
    numbers_arr = []
    for char in line:
        if char.isdigit():
            numbers_arr.append(char)
    
    num = numbers_arr[0] + numbers_arr[-1]
    s += int(num)

print(s) #54634