import random

# start = "n"
# while(start != "y"):
#     start = input("Are you ready? (y/n) \n")

while(1):
    key = {"r":1, "p":2, "s":3}
    n = input("Your turn: ")
    npc = random.randrange(1, 4)
    
    if n not in key.keys():
        print("Enter a key: R, P, or S \n")
        continue
    
    player = key[n]
    if player == npc:
        print("It's a draw")
    

print("Game Finished.")