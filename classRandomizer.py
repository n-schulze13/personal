import random

participants = []

while True:
    name = input("Please enter the names of the students: ")
    if name == "END":
        break
    else:
        participants.append(name)

print(participants)

    