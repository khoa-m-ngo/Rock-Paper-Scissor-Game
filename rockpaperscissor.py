import random

# start = "n"
# while(start != "y"):
#     start = input("Are you ready? (y/n) \n")
point = {"player": 0, "npc": 0}
key = {"r":1, "p":2, "s":3, "1":"Rock", "2":"Paper", "3":"Scissor"}

while(1):
    n = input("Your turn: \n")
    npc = random.randrange(1, 4)

    if n not in key.keys():
        print("Enter a key: R, P, or S \n")
        continue
    
    player = key[n]
    if player == npc:
        print("It's a draw")
    elif player == 1 and npc == 2:
        point["npc"] += 1
    elif player == 1 and npc == 3:
        point["player"] += 1
    elif player == 2 and npc == 1:
        point["player"] += 1
    elif player == 2 and npc == 3:
        point["npc"] += 1
    elif player == 3 and npc == 1:
        point["npc"] += 1
    elif player == 3 and npc == 2:
        point["player"] += 1
    
    print("You chose " + key[str(player)] + ". Opponent chose " + key[str(npc)])
    print(str(point) + "\n")

    if point["player"] >= 3:
        print("You won! \n")
        break
    elif point["npc"] >= 3:
        print("You lost... \n")
        break

print("Game Finished.")