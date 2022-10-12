#Write your code below this line 👇

def prime_checker(number):

    if number < 2:
        return False
    
    #prime number can not be divided by any other number other than itself
    last_to_check = int(number ** 0.5)
    for i in range(2, last_to_check):
        if number%i == 0:
            return False

    return True


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
is_prime = prime_checker(number=n)

if is_prime:
    print("It's a prime number.")
else:
    print("It's not a prime number.")




