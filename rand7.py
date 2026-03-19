import random

# Function that returns a random number from 1 to 5
def rand5():
    return random.randint(1, 5)

# Function to generate a random number from 1 to 7
def rand7():
    while True:
        # Combine two rand5() calls to get range 1–25
        num = (rand5() - 1) * 5 + rand5()

        # Accept only values from 1–21
        if num <= 21:
            return (num % 7) + 1

# Test the function
for _ in range(10):
    print(rand7())
