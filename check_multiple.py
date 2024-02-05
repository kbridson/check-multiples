import random


def check_multiple(number, divisor):
    if number % divisor == 0:
        print(f"{number} is evenly divisible by {divisor}")
    else:
        print(f"{number} is evenly divisible by {divisor}")


number = random.randint(1, 100)
divisor = random.randint(1, 10)
check_multiple(number, divisor)
