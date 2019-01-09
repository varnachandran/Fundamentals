import random

def rand7():
    return random.randint(1,7)

def simulate_5sided_die():
    number = rand7()
    while number > 5:
        number = rand7()
    return number

def simulate_recursion():
    number = rand7()
    if number > 5:
        number= simulate_recursion()
    return number

print(simulate_recursion())