import random

def randomize_list(names, force_end_names=[]):
    
    # Create a copy of the names list to avoid modifying the original
    names_copy = names.copy()

    # Convert force_end_names to a set to remove duplicates
    unique_force_end_names = set(force_end_names)

    # Remove the forced names from the copy
    for name in unique_force_end_names:
        if name in names_copy:
            names_copy.remove(name)

    # Randomize the remaining names
    random.shuffle(names_copy)

    # Add the forced names to the end
    names_copy.extend(unique_force_end_names)

    return names_copy

if __name__ == "__main__":
    names = input("Enter names, separated by commas: ").split(", ")
    force_end_names = input("Enter names to force to the end, separated by commas: ").split(", ")

    randomized_names = randomize_list(names, force_end_names)
    print(randomized_names)