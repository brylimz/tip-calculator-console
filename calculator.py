print("Welcome to the tip calculator")
bill = input("What was the total bill ?\n")
split = input("How many people to split the bill \n")
percentage = input("What percentage tip would you like to give 10, 12, or 15 ?\n")
bill = float(bill)
split = int(split)
percentage = float(percentage) / 100
abc = bill + (bill * percentage)
dbe = round((abc/split),2)
print(dbe)

