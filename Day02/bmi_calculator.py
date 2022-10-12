height = float(input('Enter your height in m: '))
weight = float(input('Enter your weight in kg: '))
bmi = weight / (height**2)
print(f'Your body mass index is {int(bmi)}')