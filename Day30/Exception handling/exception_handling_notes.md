# Exception handling in python

```python
try:
    # code that can throw exception
except ErrorName as error:
    # run this code if an exception is thrown
else:
    # run this code if an exception is NOT thrown
finally:
    # run this code regardless of whether an exception is thrown on not
    # Basically this block runs everytime
```

## Most common errors in python
```python
# 1. IndexError
lst = [1, 2, 3]
print(lst[3])

# 2. KeyError
dct = {'a': 'A', 'b': 'B'}
print(dct['c'])

# 3. TypeError
n1 = 5
n2 = '4'
print(n1+n2)

# 4. FileNotFoundError
file = open('does_not_exist.txt')
```


