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

number = -3
number2 = 0

class Text:
    def __init__(self, canvas, pos_x, pos_y, size, color, var_text):
        self.canvas = canvas
        self.id = canvas.create_text(pos_x, pos_y, fill=color, font=("Purisa", size), text="%s" % var_text)

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
        
    def draw(self, paddle):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        self.paddle = paddle
        if pos[1] <= 0:
            global number
            self.y = abs(number)
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            global number
            global number2
            number2 += 1
            if paddle.x == -2.50:
                number -= 0.2
                self.y = number
                self.x = -3
                self.canvas.itemconfig(points.id, text="Points: %s" % str(number2))
            elif paddle.x == 2.50:
                number -= 0.2
                self.y = number
                self.x = 3
                self.canvas.itemconfig(points.id, text="Points: %s" % str(number2))
            else:
                self.canvas.itemconfig(points.id, text="Points: %s" % str(number2))
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
        self.x = -2.50
    def turn_right(self, evt):
        self.x = 2.50

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'orange')

points = Text(canvas, 250, 15, 14, "Slate Gray", "Points: %s" % str(number2))
arrow_left = Text(canvas, 50, 15, 12, "Gray", "Arrow Left: Left")
arrow_right = Text(canvas, 442, 15, 12, "Gray", "Arrow Right: Right")

while 1:
    if ball.hit_bottom == False:
        ball.draw(paddle)
        paddle.draw()
    elif ball.hit_bottom == True:
        Text(canvas, 250, 100, 20, "Red", "Game Over!")
        Text(canvas, 250, 140, 14, "Green", "To close the game hit the Red/Gray X button, then hit Terminate.")
        canvas.itemconfig(points.id, text="Total Points: %s" % str(number2))
        canvas.move(points.id, 0, 106)
        canvas.move(arrow_left.id, 1000, 1000)
        canvas.move(arrow_right.id, 1000, 1000)
        ball.hit_bottom = None
    
    tk.update_idletasks()
    tk.update()
