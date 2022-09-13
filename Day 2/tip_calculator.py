print('Welcome to the tip calculator.')
bill = float(input('What was the total bill? $'))
people = int(input('How many people to split the bill? '))
tip_perc = float(input('What percentage tip would you like to give? 10, 12, or 15 '))

bill_and_tip = bill + bill * (tip_perc/100)
each_person_bill = round(bill_and_tip / people,2)

print(f'Each person should pay: ${each_person_bill}')