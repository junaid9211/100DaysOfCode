# Exercise 1: square numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n**2 for n in numbers]
print(squared_numbers)

# Exercise 2: even numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
even_numbers = [n for n in numbers if n%2 == 0]
print(even_numbers)

# Exercise 3: data overlap
with open('file1.txt') as file1:
    file1_data = file1.readlines()

with open('file2.txt') as file2:
    file2_data = file2.readlines()

result = [int(num) for num in file1_data if num in file2_data]
print(result)

# Exercise 4: dictionary comprehension 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)


# Exercise 5: dictionary comprehension 2
weather_c = {
    'Monday': 12,
    'Tuesday': 14,
    'Wednesday': 15,
    'Thursday': 14,
    'Friday': 21,
    'Saturday': 22,
    'Sunday': 24,
}
weather_f = {day: (temp_c*9/5) + 32 for day, temp_c in weather_c.items()}
print(weather_f)
