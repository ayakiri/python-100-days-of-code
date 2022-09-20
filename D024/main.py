import re

with open("Inputs/Letters/blank_letter.txt") as blank_letter:
    letter = blank_letter.read()

with open("Inputs/Guests/invited_names.txt") as invited_names:
    guests = invited_names.read().split("\n")

for guest_name in guests:
    completed_letter = re.sub("\[name]", guest_name, letter)
    path = "Outputs/Letters/letter_for_" + re.sub("(\s)", "_", guest_name).lower() + ".txt"
    with open(path, mode="w") as save_letter:
        save_letter.write(completed_letter)
    print(f"Letter for {guest_name} saved")

print("Completed creating letters")
