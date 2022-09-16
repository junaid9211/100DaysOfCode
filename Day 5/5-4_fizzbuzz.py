# commmon Fizzbuzz problem
# The program should print each number from 1 to 100 in turn.

# When the number is divisible by 3 then instead of printing the number it should print "Fizz".

# When the number is divisible by 5, then instead of printing the number it should print "Buzz".

# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for i in range(1, 101):
    divisible_by_3 = i % 3 == 0
    divisible_by_5 = i % 5 == 0
    if divisible_by_3 and divisible_by_5:
        print('FizzBuzz')
    elif divisible_by_3:
        print('Fizz')
    elif divisible_by_5:
        print('Buzz')
    else:
        print(i)
