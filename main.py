#If the bill was $150.00, split between 5 people, with 12% tip.
print()
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.\n")
total_bill = input("What was the total bill? $")
perc_tip = input("What percentage tip would you like to give? 10,20, or 15? ")
people_split_bill = input("How many people to split the bill? ")
each_pay = round(float(total_bill)/float(people_split_bill)*1.12,2)
print(f"Each person should pay: ${each_pay}")