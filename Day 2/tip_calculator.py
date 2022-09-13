print('Welcome to the tip calculator.')
bill = input('What was the total bill? $')
people = input('How many people to split the bill? ')
tip_perc = input('What percentage tip would you like to give? 10, 12, or 15 ')

bill_and_tip = float(bill) + float(bill)*(float(tip_perc)/100)
each_person_bill = round(bill_and_tip / int(people),1)

print(f'Each person should pay: ${each_person_bill}')