print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percetange tip would like to give? 10, 12 15? "))
persons = int(input("How many people will split the bill?"))
the_whole_bill = tip / 100 * bill +bill
print(the_whole_bill)
print(f"Each person will have to pay: {the_whole_bill / persons} dollars")
print(round(the_whole_bill / persons), "dollars")