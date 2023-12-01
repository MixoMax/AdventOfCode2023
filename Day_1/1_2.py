#Advent of Code 2023 Day 1 Part 2

with open("data.txt", "r") as f:
    input_lines = f.readlines()
input_lines: list[str] = [line.replace("\n", "") for line in input_lines]


number_dict = {
    #edge cases
    "oneight": "18",
    "twone": "21",
    "threeight": "38",
    "fiveight": "58",
    "sevenine": "79",
    "eightwo": "82",
    "eighthree": "83",
    "nineight": "98",
    
    #regular cases
    "one": "1",
    "two": "2",
    "three": "3", 
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


s = 0
for line in input_lines:
    
    for key, val in number_dict.items():
        line = line.replace(key, val)
        
    num_arr = []
    for char in line:
        if char in number_dict.values():
            num_arr.append(char)

    num = num_arr[0] + num_arr[-1]
    s += int(num)

print(s) #53855