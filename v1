import tkinter as tk
import time
class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.root = master
        self.lives = 0
        self.width = 330
        self.height = 500
        self.canvas = tk.Canvas(self, bg='#aaaaff',
                                width = self.width,
                                height = self.height)
        self.canvas.pack()
        self.pack()

        self.items = {}
        self.ball1 =None
        self.ball2 =None
        self.ball3 =None
        self.ball4 =None
        self.ball5 =None
        self.canvas.focus_set()

        self.add_ball()
        self.start_game()

    def add_ball(self):

        self.ball1 = Ball(self.canvas, 35, 50,1,0,"red")
        self.items[self.ball1.item] = self.ball1
        self.ball2 = Ball(self.canvas, 100, 50,1,0,"red")
        self.items[self.ball2.item] = self.ball2

        self.ball3 = Ball(self.canvas, 165, 50,1,0,"red")
        self.items[self.ball3.item] = self.ball3

        self.ball4 = Ball(self.canvas, 230, 50,1,0,"red")
        self.items[self.ball4.item] = self.ball4

        self.ball5 = Ball(self.canvas, 295, 50,1,0,"red")
        self.items[self.ball5.item] = self.ball5

    def move(self, x, y):
        self.canvas.move(self.item, x, y)

    def start_game(self):
        self.game_loop()

    def game_loop(self):
        self.check_collisions()
        self.ball1.update(None)
        self.ball2.update(None)
        self.ball3.update(None)
        self.ball4.update(None)
        self.ball5.update(None)
        self.after(50, self.game_loop)

    def check_collisions(self):
        X1 =[]
        X = []
        tags = self.canvas.find_all()  # finds tags of all the object created
        for tag in tags:
            x0, y0, x1, y1 = self.canvas.coords(tag)  # corresponding coordinates
            center = [(x0 + x1) / 2, (y0 + y1) / 2]  # centers of objects
            X.append(center)
            coords1 = [x0,y0,x1,y1]
            X1.append(coords1)
            print("x1",X1)
        print("çıktı")
        for k in X:
            #print("11.deger:", abs(X[0][0] - X[1][0]) )
            while (abs(X[0][0] - X[1][0]) <= 60) and (abs(X[0][1] - X[1][1]) <= 60):

                a=1
                #print("11.deger:",X[0][0] - X[1][0])
                #print("12.deger:", X[0][1] - X[1][1])
                print("bingo:",a)
                print("k:", k)
                self.ball1.update(a)
                self.ball2.update(a)
                self.ball3.update(a)
                self.ball4.update(a)
                self.ball5.update(a)

                break

            X.clear()
        a=0





class GameObject(object):
    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item

    def get_position(self):
        return self.canvas.coords(self.item)

    def move(self, x, y):
        self.canvas.move(self.item, x, y)


class Ball(GameObject):

    def __init__(self, canvas, d, h, xVelocity, yVelocity,color):
        self.width = 30
        self.height = 30
        self.gravity = 0.7
        self.friction = 0.5
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

        item = canvas.create_oval(d - self.width ,
                                       h - self.height ,
                                       d + self.width ,
                                       h + self.height ,
                                       fill=color, tags='ball')

        super(Ball, self).__init__(canvas, item)

    def update(self,a):

        coords = self.get_position()
        if coords[3] >= 500 and self.yVelocity < 0.001:
            self.xVelocity = 0
            self.yVelocity = 0
            self.friction = 0
            self.gravity = 0
            print("1")

        if coords[3] >= 500 or coords[1] <0:

            self.yVelocity *= -1
            print("2")

        if coords[2] >=330 or coords[0]<=0:
            print("3")
            self.xVelocity = -(self.xVelocity * self.friction)
            print("xVeelocity",self.xVelocity)

        if a ==1:
            print("move1:",self.xVelocity, self.yVelocity)
            self.xVelocity *= -1
            self.yVelocity *= -1
            print("move2:", self.xVelocity, self.yVelocity)

        self.yVelocity += self.gravity

        self.move(self.xVelocity, self.yVelocity)
        print("move3:", self.xVelocity, self.yVelocity)







if __name__ == '__main__':
    root = tk.Tk()
    root.title("Hello Pong!")
    game = Game(root)
    game.mainloop()
