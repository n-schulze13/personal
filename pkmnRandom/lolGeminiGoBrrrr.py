import random

def main():
    region_choices = {
        "K": 151,
        "J": 256,
        "H": 202,
        "S": 210,
        "I": 242,
        "U": 155,
        "L": 457,
        "A": 302,
        "G": 400,
        "P": 400,
    }

    region_choice = input("What region's Pokedex would you like to use? Default is National. Please enter [letter] - [K]anto, [J]ohto, [H]oenn, [S]innoh, H[i]sui, [U]nova, Ka[l]os, [A]lola, [G]alar, [P]aldea: ").upper()
    pcount = input("How many players are there? ")

    try:
        dex_size = region_choices[region_choice]
    except KeyError:
        print("Invalid region choice. Using National Dex.")
        dex_size = 1025

    try:
        player_count = int(pcount)
    except ValueError:
        print("Invalid player count. Using default value of 2.")
        player_count = 2

    # Generate a list of unique random numbers within the dex size
    choices = random.sample(range(1, dex_size + 1), player_count * 6)

    # Divide the choices into teams
    player_teams = []
    for i in range(player_count):
        player_teams.append(choices[i*6:(i+1)*6])

    print(player_teams)

if __name__ == "__main__":
    main()