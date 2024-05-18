def print_numbers(n):
    numbers = range(n)
    for number in numbers:
        print (number) 


# if statement
def print_even_numbers(n):
    numbers = range(n)
    for number in numbers:
        if number%2 == 0:
            print(number)

# else statement
def odd_or_even(n):
    numbers = range(n)
    for number in numbers:
        if number%2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")

# elif statement
def check_divisibility(n):
    numbers = range(n)
    for number in numbers:
        if number%3 == 0:
            print(f"{number} is divisible by 3")
        elif number%5 == 0:
            print(f"{number} is divisible by 5")
        elif number%7 == 0:
            print(f"{number} is divisible by 7")
        else:
            print(f"{number} is not divisble by 3,5 , or 7")

# while statement; continues running while the condition is true
def count_down(n):
    x = 0
    while n > x:
        print(n)
        n-=1

# break
def count_down_to_five(n):
    x = 0
    while n > x:
       
        if n==5:
            break
        print(n)
        n-=1


# continue statement
def divisible_by_seven(n):
    x = 1
    while x <= n:
          x += 1
          if x%7!= 0:
            continue
    print(f"{x} is divisble by 7")  

#qn1
def odd_number():
    num = 0
    while num <= 100:
        if num % 2 != 0:
            print(num)
            continue
        num += 1
odd_number()
# qn 2
def fizz_buzz(n):
    numbers = range(n)
    for number in numbers:
        if number%3 == 0:
            print(f"{number} :fizz")
        elif number%5 == 0:
            print(f"{number} :buzz")
        else:
            print(f"{number} :fizzbuzz")

