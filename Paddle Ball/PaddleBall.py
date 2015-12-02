try:
    from Tkinter import *
except ImportError:
    from tkinter import *

import random
import time

tk = Tk()
tk.title("PaddleBall")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

over = True
number = -3
number2 = 0

class Text:
    def __init__(self, canvas, pos_x, pos_y, size, color, var_text):
        self.canvas = canvas
        self.id = canvas.create_text(pos_x, pos_y, fill=color, font=("Purisa", size), text="%s" % var_text)

my_score0 = canvas.create_text(80, 80, fill='green', font=("Purisa", 12), text="Points: 0")        

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            global number
            self.y = abs(number)
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            global number
            global number2
            global my_score0
            canvas.move(my_score0, -1000, -1000)
            number2 += 1
            my_score0 = canvas("Portal: " + str(number2))
            if number >= -5:
                number -= 0.2
                self.y = number
            else:
                self.y = number
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
            
    def turn_left(self, evt):
        self.x = -2.75
    def turn_right(self, evt):
        self.x = 2.75

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'orange')

while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    elif ball.hit_bottom == True and over == True:
        text = Text(canvas, 250, 100, 20, "red", "Game Over!")
        text2 = Text(canvas, 250, 120, 14, "green", "Total Points: %s" % str(number2))
        over = False
        
    tk.update_idletasks()
    tk.update()
