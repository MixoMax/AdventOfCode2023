#Advent of Code 2023 Day 4 Part 2

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Game:
    def __init__(self, game_str):
        self.id:int = int(game_str[4:game_str.index(": ")])
        
        self.amount = 1
        
        left, right = game_str.split(" | ")
        
        right = right.replace("  ", " ")
        
        left = left.split(": ")[-1]
        left = left.replace("  ", " ")
        
        self.left_nums = []
        self.right_nums = []
        
        for num in left.split(" "):
            try:
                self.left_nums.append(int(num))
            except:
                pass
            
        for num in right.split(" "):
            try:
                self.right_nums.append(int(num))
            except:
                pass

    
    def calculate_union(self):
        #calculate the union of the sets of numbers
        #(overlap)
        return list(set(self.left_nums) & set(self.right_nums))


    def add_winnings(self, games):
        num_matches = len(self.calculate_union())
        for i in range(1, num_matches + 1):
            next_card_id = self.id + i
            if next_card_id in games:
                games[next_card_id].amount += self.amount

    def __str__(self):
        return f"{self.amount} * Card {self.id}: {self.calculate_union()}"        


with open("data.txt", "r") as f:
    input_lines = [line.strip() for line in f.readlines()]

games = {i: Game(line) for i, line in enumerate(input_lines, start=1)} # id: Game

changes = True
while changes:
    changes = False
    for game in list(games.values()):
        initial_amount = game.amount
        game.add_winnings(games)
        if game.amount != initial_amount:
            changes = True

total_cards = sum(game.amount for game in games.values())

print(total_cards)