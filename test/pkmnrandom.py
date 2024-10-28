# pokemon randomizer - will read the pokedex csv file and take specifications to output a list of mons for a draft!

import pandas as pd
import csv
import sys

def main():
    """if len(sys.argv) != 2:
        print("Usage: python pkmnrandom.py pokemon.csv")
        sys.exit(1)"""
    
    # read the csv into a variable
    # df = pd.read_csv(sys.argv[1])

    with open('./test/pokemon.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)  # Each row is a list of values
    

main()
