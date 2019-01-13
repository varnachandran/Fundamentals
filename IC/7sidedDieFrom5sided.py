import random

def simulate_7_sided_die():
    result = (random.randint(1,5) - 1) *5 + random.randint(1,5)

    while result > 21:
        result = (random.randint(1, 5) - 1) * 5 + random.randint(1, 5)
    return result % 7 +1

print simulate_7_sided_die()