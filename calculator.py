# return 
def add(x,y):
    result = x + y
    return result
def subtract(x,y):
    result = x-y
    return result
def divide(x,y):
    result = x/y
    return result
def multiply(x,y):
    result = x*y
    return result
def remainder(x,y):
    result = x%y
    return result
def power_of(x,y):
    result = x**y
    return result
# functions that adds multiple nubers
def sum(*numbers):
    print(numbers)
    total = 0
    for number in numbers:
        total += number
    return total 
# A function that can multiply any number of numbers
def multiply_many(*nums):
    total =1
    for number in nums:
        total *= number
    return total
# Add *args and **kwargs
def sum_and_greet(*args,**kwargs):
    total = 0
    for x in args:
        total += x
    f = kwargs["firstname"]
    l = kwargs["lastname"]
    greeting = f"Hello {f} {l}, the sum of your numbers is `{total}`"
    return greeting