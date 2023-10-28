import random

def play():
    while True:
        user = input("What's your 'choice? enter rock, paper, scissor or quit\n").lower()
        computer = random.choice(["rock", "paper", "scissor"])

        if user == computer:
            print("~~~~Tie~~~~")
    
        if is_win(user, computer):
            print("!!!!You win!!!!")
        
            
        if user == "quit":
            break

        if (is_win(user, computer)==False):
            print("$$$$YOU LOST$$$$")


def is_win(player, opponent):
    if (player=="rock" and opponent=="scissor")or (player=="scissor" and opponent=="paper") or (player=="paper" and opponent=="rcok"):
        return True
    if (opponent=="rock" and player=="scissor") or (opponent=="scissor" and player=="paper") or (opponent=="paper" and player=="rock"):
        return False
    
print(play())
