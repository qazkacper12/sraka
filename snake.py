from tkinter import *
import random

GAME_WITDH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"

class snake:
    

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR, tag = "snake")
            self.squares.append(square)

class food:
    def __init__(self):

        x = random.randint(0, (GAME_WITDH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE)-1) * SPACE_SIZE

        self.coordonates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill =FOOD_COLOR, tag="food" )   
def next_turn(snake, food):
    
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":
        y += SPACE_SIZE

    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":
        x += SPACE_SIZE

snake.coordinates.insert(0, (x, y))

square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR)

snake.squares.insert(0, square)

del snake.coordinates[-1]

canvas.delete(snake.squares[-1])

canvas.delete(snake.squares[-1])

del snake.squares

window.after(SPEED, next_turn, snake, food)



def change_direction(new_directon):
    pass

def chec_collisions():
    pass

def game_over():
    pass

window = Tk()
window.title("WĘŻYK")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="punkty:{}".format(score), font =('consolas',40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height = GAME_HEIGHT, width = GAME_WITDH)
canvas.pack()

window.update()

window_witdh = window.winfo_width()
window_height = window.winfo_height()
screen_witdh = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x= int((screen_witdh/2) - (window_witdh/2))
y= int((screen_height/2) - (window_height/2))

window.geometry(f"{window_height}x{window_height}+{x}+{y}")

snake = snake()
food = food()

next_turn(snake, food)

window.mainloop()