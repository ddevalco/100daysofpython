# Tip Calculator

print("Welcome to the tip calculator.")

total = input("What was the total bill?")

people = input("How many people to split the bill?")

tip = input("What % tip would you like to give? 10, 15 or 20?")

tiptotal = int(total) * (float(tip) / 100)
print (tiptotal)
subtotal = int(tiptotal) + int(total)
print (subtotal)
ppperson = int(subtotal) / int(people)

print("Each person should pay: " + str(float(ppperson)))