#Advent of Code 2023 Day 3 Part 1

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("./data.txt", "r") as f:
    input_lines = f.readlines()
input_lines = [line.replace("\n", "") for line in input_lines]


#we store all the locations of all chars thar are not 0-9 and "."
part_locations = []

for y in range(len(input_lines)):
    for x in range(len(input_lines[y])):
        char = input_lines[y][x]
        if char not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
            part_locations.append((x,y)) #x,y

#for each part location we look at the eight neighbours (left, right, up, down and the 4 diagonals)
#if they are a number (0-9), append their locations to a new list
num_locations = []

for tup in part_locations:
    x, y = tup
    
    neighbors = [
        (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
        (x - 1, y),                     (x + 1, y),
        (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)
    ]
    #filter out indecis out of range
    
    for cord in neighbors:
        x_new, y_new = cord
        if y_new > len(input_lines) - 1:
            break
        line = input_lines[y_new]
        if x_new > len(line) - 1:
            break
        char: str = line[x_new]
        
        if char.isdigit():
            num_locations.append((x_new, y_new))


#now we have all locations of single digit numbers neighboring a part

s = 0

for idx, line in enumerate(input_lines):
    locs = []
    for loc in num_locations:
        if loc[1] == idx:
            locs.append(loc[0])
    
    temp_num_str = ""
    is_valid = False
    for x, char in enumerate(line):
        #if char.isdigit(): append it to temp_num_str
        #if cords of char in locs it is legit:
        if char in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            temp_num_str += char
            if x in locs:
                is_valid = True
        else:
            if temp_num_str and is_valid:
                s += int(temp_num_str)
            temp_num_str = ""

print(s)