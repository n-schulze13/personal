import random

def main():
    
    choices = []
    dex = []

    regionChoice = input("What region's pokedex would you like to use? Default is National. Please enter [letter] - [K]anto, [J]ohto, [H]oenn, [S]innoh, H[i]sui, [U]nova, Ka[l]os, [A]lola, [G]alar, [P]aldea: ")
    pcount = input("How many players are there? ")
    
# switch for region entry to set a dex size
    match regionChoice.capitalize:
        case 'K':
            dex = [151]
        case 'J':
            dex = [256]
        case 'H':
            dex = [202]
        case 'S':
            dex = [210]
        case 'I':
            dex = [242]
        case 'U':
            dex = [155]
        case 'L':
            dex = [457]
        case 'A':
            dex = [302]
        case 'G':
            dex = [400]
        case 'P': 
            dex = [400]
        case _:
            dex = [1025]

    for i in range(int(pcount)*6):
        mon = random.randint(1,max(dex))
        while mon in choices:
            random.randint(1,max(dex))
        choices.append(mon)

    print(choices)

main()