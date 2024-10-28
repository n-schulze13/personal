import random

def main():
    dex = []
    choices = []
    dexSize = input("How many pokemon in the pokedex?: ")
    pcount = input("How many players are there? ")
    for i in range(int(dexSize)):
        dex.append(i+1)
    
    for i in range(int(pcount)*6):
        mon = random.randint(1,max(dex))
        if mon in choices:
            continue
            #reroll choice
        else:
            choices.append(mon)


    print(choices)

main()