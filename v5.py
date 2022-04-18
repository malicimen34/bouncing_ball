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
                                width=self.width,
                                height=self.height)
        self.canvas.pack()
        self.pack()
        self.q = None
        self.w = None
        self.mouse_x = 0
        self.mouse_y = 0
        self.x0 = None
        self.y0 = None
        self.x1 = None
        self.y1 = None

        self.items = {}
        self.canvas.focus_set()
        self.add_ball()
        self.start_game()

    def add_ball(self):

        self.ball1 = Ball(self.canvas, 35, 50, 0, -1, "green")
        self.items[self.ball1.item] = self.ball1

        self.ball2 = Ball(self.canvas, 100, 50, 0, -1, "red")
        self.items[self.ball2.item] = self.ball2

        self.ball3 = Ball(self.canvas, 165, 50, 0, -1, "blue")
        self.items[self.ball3.item] = self.ball3

        self.ball4 = Ball(self.canvas, 230, 50, 0, -1, "black")
        self.items[self.ball4.item] = self.ball4

        self.ball5 = Ball(self.canvas, 295, 50, 0, -1, "white")
        self.items[self.ball5.item] = self.ball5

    def start_game(self):
        self.game_loop()

    def game_loop(self):
        self.check_collisions()
        self.click_check()
        self.ball1.update(None, None, None)
        self.ball2.update(None, None, None)
        self.ball3.update(None, None, None)
        self.ball4.update(None, None, None)
        self.ball5.update(None, None, None)
        self.after(50, self.game_loop)

    def callback(self, e):
        self.mouse_x = e.x
        self.mouse_y = e.y
        # print("Pointer is currently at %d, %d" % (self.mouse_x, self.mouse_y))

    def check_collisions(self):
        Y = []
        X = []
        t = 0
        a = 0
        tags = self.canvas.find_all()  # finds tags of all the object created
        bircks=[None,"ball1","ball2","ball3","ball4","ball5"]
        # print(self.q,self.w)
        for tag in tags:
            #print("tag:", tag)
            x0, y0, x1, y1 = self.canvas.coords(tag)  # corresponding coordinates
            center = [(x0 + x1) / 2, (y0 + y1) / 2]  # centers of objects
            #print(type(center[0]))
#            while center[0]+-30 <= 0 or center+30 >= 500:
#                pass
#                self.tags[1].update(a, None, None)

            X.append(center)
            coords1 = [x0, y0, x1, y1]
            Y.append(coords1)

            # print("y:", Y)
            #print("x:", X)
        list = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        # print("çıktı")
        for k in list:
            k1 = k[0]
            k2 = k[1]
            #print("k", k)
            # print("k,j:", k,j)
            while ((abs(X[k1][0] - X[k2][0]) <= 60) and (abs(X[k1][1] - X[k2][1]) <= 60)):

                # Right

                while (round(Y[k1][2], 3) < round(Y[k2][0], 3)) and a != 1:
                    a = 1
                    print("a:", a)
                    # print("k=",k)
                    # print("j=",j)
                    print("11")
                    break
                # Left
                while (round(Y[k1][0], 3) > round(Y[k2][2], 3)) and a != 2:
                    a = -1
                    print("a:", a)
                    # print("k=", k)
                    # print("j=", j)
                    print("22")
                    break
                # Up
                while (round(Y[k1][3], 3) > round(Y[k2][1], 3)) and a != 3:
                    a = 2
                    print("a:", a)
                    # print("k=", k)
                    # print("j=", j)
                    print("33")
                    break
                # Down
                while round(Y[k1][1], 3) < round(Y[k2][3], 3) and a != 4:
                    a = -2
                    print("a:", a)
                    # print("k=", k)
                    # print("j=", j)
                    print("44")
                    break
                # print("bingo:", a)
                # print("k:", k)
                while k == [0, 1]:
                    self.ball1.update(a, None, None)
                    self.ball2.update(-a, None, None)
                    print("A1")
                    break
                while k == [0, 2]:
                    self.ball1.update(a, None, None)
                    self.ball3.update(-a, None, None)
                    print("A2")
                    break
                while k == [0, 3]:
                    self.ball1.update(a, None, None)
                    self.ball4.update(-a, None, None)
                    print("A3")
                    break
                while k == [0, 4]:
                    self.ball1.update(a, None, None)
                    self.ball4.update(-a, None, None)
                    print("A4")
                    break
                while k == [1, 2]:
                    self.ball2.update(a, None, None)
                    self.ball3.update(-a, None, None)
                    print("A5")
                    break
                while k == [1, 3]:
                    self.ball2.update(a, None, None)
                    self.ball4.update(-a, None, None)
                    print("A6")
                    break
                while k == [1, 4]:
                    self.ball2.update(a, None, None)
                    self.ball5.update(-a, None, None)
                    print("A7")
                    break
                while k == [2, 3]:
                    self.ball3.update(a, None, None)
                    self.ball4.update(-a, None, None)
                    print("A8")
                    break
                while k == [2, 4]:
                    self.ball3.update(a, None, None)
                    self.ball5.update(-a, None, None)
                    print("A9")
                    break
                while k == [3, 4]:
                    self.ball4.update(a, None, None)
                    self.ball5.update(-a, None, None)
                    print("A9")
                    break
                break
            # a = 0

    def click_check(self):
        self.canvas.bind('<ButtonPress-1>', self.callback)
        tags = self.canvas.find_all()
        X1 = []
        Y1 = []
        counter = 0
        for tag in tags:
            x0, y0, x1, y1 = self.canvas.coords(tag)
            center_x = (x0 + x1) / 2
            center_y = (y0 + y1) / 2
            # X1.append(center)
            coords2 = [x0, y0, x1, y1]
            Y1.append(coords2)
            counter += 1
            while self.mouse_x >= x0 and self.mouse_x <= x1 and self.mouse_y >= y0 and self.mouse_y <= y1:
                print("mouse")
                #print(type(center_x))
                x_move = (center_x - self.mouse_x)
                y_move = (center_y - self.mouse_y)
                a = 5
                while counter == 1:
                    print("a1")
                    self.ball1.update(a, x_move, y_move)
                    #counter = 0
                    break
                while counter == 2:
                    print("a2")
                    self.ball2.update(a, x_move, y_move)
                    #counter = 0
                    break
                while counter == 3:
                    print("a3")
                    self.ball3.update(a, x_move, y_move)
                    break
                    #counter = 0
                while counter == 4:
                    self.ball4.update(a, x_move, y_move)
                    break
                    #counter = 0
                while counter == 5:
                    self.ball5.update(a, x_move, y_move)
                    break
                    #counter = 0
                self.mouse_x = 0
                self.mouse_y = 0
                break

            # print("X1:",X1)


class GameObject(object):
    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item

    def get_position(self):
        return self.canvas.coords(self.item)

    def move(self, x, y):
        self.canvas.move(self.item, x, y)


class Ball(GameObject):

    def __init__(self, canvas, d, h, xVelocity, yVelocity, color):
        self.width = 30
        self.height = 30
        self.gravity = 0.7
        self.friction = 1
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
        self.a_counter =0
        item = canvas.create_oval(d - self.width,
                                  h - self.height,
                                  d + self.width,
                                  h + self.height,
                                  fill=color, tags='ball')

        super(Ball, self).__init__(canvas, item)

    def update(self, a, center_x, center_y):

        coords = self.get_position()
        print("a_counter:" ,self.a_counter)
        while coords[3] >= 500 and self.yVelocity < 1:
            self.xVelocity = 0
            self.yVelocity = 0
            self.friction = 0
            self.gravity = 0
            print("b1")
            break
        while (coords[3] >= 500 or coords[1] < 0 or a == 1 or a == 2 ):
            self.yVelocity *= -1

            print("b2")
            break


        while (coords[2] >= 330 or coords[0] <= 0 or a == 3 or a == 4):
            print("b3")
            self.xVelocity *= -1
            break
            # print("xVeelocity", self.xVelocity)

        while a==1:
            while self.xVelocity < 0:
                self.xVelocity *= 1
                break
            while self.xVelocity > 0:
                self.xVelocity *=-1
                break
            break

        while a==-1:
            while self.xVelocity < 0:
                self.xVelocity *= -1
                break
            while self.xVelocity > 0:
                self.xVelocity *= 1
                break
            break


        while a==2:
            while self.yVelocity < 0:
                self.yVelocity *= 1
                break
            while self.yVelocity > 0:
                self.yVelocity *=-1
                break
            break
        while a==-2:
            while self.yVelocity < 0:
                self.yVelocity *= -1
                break
            while self.yVelocity > 0:
                self.yVelocity *= 1
                break
            break


        while a == 5:
            print("centerx:", center_x)
            print("centery:", center_y)
            self.xVelocity = center_x
            self.yVelocity = center_y
            a = 0
            break
        self.yVelocity += self.gravity
        print("xVelo:", self.xVelocity)
        print("yVelo:", self.yVelocity)
        self.move(self.xVelocity, self.yVelocity)
        # print("move3:", self.xVelocity, self.yVelocity)


while __name__ == '__main__':
    root = tk.Tk()
    root.title("Bouncing Ball")
    game = Game(root)

    game.mainloop()
    break

