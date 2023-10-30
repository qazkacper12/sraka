import random

num = random.randint(1, 10)
guess = None

while guess != num:
    guess = input("""Zgadnij numer między 1 a 10
>>> """)
    guess = int(guess)

if guess == num:
    print("Gratulacje, wygrałeś!")
    breakpoint
else:
    print("Źle")