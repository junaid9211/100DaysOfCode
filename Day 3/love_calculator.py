# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Explaination of the formula 
# https://www.buzzfeed.com/ariannarebolini/what-are-the-chances-your-crush-is-actually-your-true-love
# WARNING it is very stupid

both_names = name1.lower()+name2.lower()
left_digit = 0
right_digit = 0

for c in 'true':
    left_digit += both_names.count(c)
for c in 'love':
    right_digit += both_names.count(c)

love_score = str(left_digit) + str(right_digit)
love_score = int(love_score)

if love_score<10 or love_score>90:
    print(f'Your score is {love_score}, you go together like coke and mentos.')
elif love_score>=40 and love_score<=50:
    print(f'Your score is {love_score}, you are alright together.')
else:
    print(f'Your score is {love_score}.')
