print("Welcome to the bill splitting/tip calculator!")

total_bill = input("What is the total bill?\n")
tip_percentage = input("What percentage tip would you like to give?\n")
number_of_people = input("How many people to split the bill?\n")

bill_per_person = (float(total_bill) + float(total_bill)*(float(tip_percentage)/100))/int(number_of_people)
bill_rounded = "{:.2f}".format(bill_per_person)

print(f"Each person should pay {bill_rounded}$")
