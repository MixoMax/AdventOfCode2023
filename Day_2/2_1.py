#Advent of Code 2023 Day 2 Part 1

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("./data.txt", "r") as f:
    input_lines = f.readlines()
input_lines = [line.replace("\n", "") for line in input_lines]

limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}

class Game:
    def __init__(self, game_str):
        self.id: int = int(game_str[5:game_str.index(":")])
        self.max_values = self.calculate_subsets(game_str)
        
    
    def calculate_subsets(self, game_str):
        out_dict = {
            "blue": 0,
            "green": 0,
            "red": 0
        }
        
        temp_str  = game_str.split(": ")[-1]
        sets = temp_str.split("; ")
        for s in sets:
            for elem in s.split(", "):
                color = ""
                for c in out_dict.keys():
                    if elem.endswith(c):
                        color = c
                
                val_old = out_dict[color]
                val_new = int(elem.split(" ")[0])
                out_dict[color] = max([val_new, val_old])
        
        return out_dict
                


games = []
for line in input_lines:
    games.append(Game(line))

s = 0

for game in games:
    if ((limits["blue"] >= game.max_values["blue"]) and
        (limits["green"] >= game.max_values["green"]) and
        (limits["red"] >= game.max_values["red"])
    ):
        s += game.id

print(s)