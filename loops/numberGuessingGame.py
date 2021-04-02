import random

num = random.randint(1, 100)
print(num)

while True:
    guess = int(input("Input your guess: "))

    if guess == num:
        print("Congrats, you got it")
        break
    elif guess > num:
        print("Try again, go down")
    else:
        print("Try again, go up")

