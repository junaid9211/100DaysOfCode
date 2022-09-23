### Scope Functions ###
    # 1. you can access global variables as constants inside function
    # 2. if you try to modify them, they will not be modified, instead a new variable will be created with the same name
    # 3. if you really want to modify a global variable then you need to use global keyword

# Example 1
print('example 1')
enemies = 1
def increase_enemies():
    # use global variables as constants (can't modify them)
    new_enemies = enemies + 5 # didn't modify enemies, just accessed it
    print(f'enemies inside function {enemies+5}')

increase_enemies()
print(f'enemies outside function {enemies}')    



# Example 2
print('example 2')
enemies = 1
def increase_enemies():
    # this will not affect the global variable enemies
    # instead, it will create a new enemies variable that is local to the function
    enemies = 2
    print(f'enemies inside function {enemies}')

increase_enemies()
print(f'enemies outside function {enemies}')  

# Example 3
print('example 3')
enemies = 1
def increase_enemies():
    global enemies
    # now you have changed the global variable enemies
    enemies= enemies + 5 
    print(f'enemies inside function {enemies}')

increase_enemies()
print(f'enemies outside function {enemies}')   


# Python has no block scope
# Creating a variable inside an if/elif or while/for
#  does not create create a local scope

# examples
for i in range(1):
    a=5
print(i, a)

if 5>2:
    var = 'inside if'
print(var)