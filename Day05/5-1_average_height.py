# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# sum() and len() functions are not allowed

height_sum = 0
number_of_heights = 0

for height in student_heights:
    height_sum += height
    number_of_heights += 1

average_heights = round(height_sum / number_of_heights)
print(average_heights)
