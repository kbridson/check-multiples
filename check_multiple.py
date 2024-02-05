def check_multiple(number, divisor):
    if number % divisor == 0:
        print(f"{number} is divisible by {divisor}")
    else:
        print(f"{number} is not divisible by {divisor}")


number = 75
divisor = 5
check_multiple(number, divisor)
