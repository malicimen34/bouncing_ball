import tkinter as tk
import time


class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.root = master
        self.lives = 0
        self.width = 500
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
        self.brick1 = None
        self.brick2 = None
        self.brick3 = None
        #self.brick4 = None
        #self.brick5 = None
        self.items = {}
        self.canvas.focus_set()
        self.add_ball()
        self.start_game()

    def add_ball(self):

        self.brick1 = Brick(self.canvas, 70, 50, 0, 1, "green")
        self.items[self.brick1.item] = self.brick1

        self.brick2 = Brick(self.canvas, 180, 50, 0, 1, "red")
        self.items[self.brick2.item] = self.brick2

        self.brick3 = Brick(self.canvas, 230, 50, 0, 1, "blue")
        self.items[self.brick3.item] = self.brick3

        self.brick4 = Brick(self.canvas, 300, 50, 0, 1, "black")
        self.items[self.brick4.item] = self.brick4

        self.brick5 = Brick(self.canvas, 370, 50, 0, 1, "white")
        self.items[self.brick5.item] = self.brick5


    def start_game(self):
        self.game_loop()

    def game_loop(self):
        self.check_collisions()
        self.click_check()
        self.brick1.update(None, None, None)
        self.brick2.update(None, None, None)
        self.brick3.update(None, None, None)
        self.brick4.update(None, None, None)
        self.brick5.update(None, None, None)
        self.after(50, self.game_loop)

    def callback(self,e):
        self.mouse_x = e.x
        self.mouse_y= e.y
        #print("Pointer is currently at %d, %d" % (self.mouse_x, self.mouse_y))

    def check_collisions(self):
        Y = []
        X = []
        t = 0
        a=0
        tags = self.canvas.find_all()  # finds tags of all the object created

        #print(self.q,self.w)
        for tag in tags:
            print("tag:",tag)
            x0, y0, x1, y1 = self.canvas.coords(tag)  # corresponding coordinates
            center = [(x0 + x1) / 2, (y0 + y1) / 2]  # centers of objects
            X.append(center)
            coords1 = [x0, y0, x1, y1]
            Y.append(coords1)


            #print("y:", Y)
            print("x:",X)
        list=[[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
        #print("çıktı")
        for k in list:
            k1=k[0]
            k2=k[1]
            print("k",k)
            #print("k,j:", k,j)
            while ((abs(X[k1][0] - X[k2][0]) <=65) and (abs(X[k1][1] - X[k2][1]) <= 65)):

                # Right

                if (round(Y[k1][2],3)< round(Y[k2][0],3)) and a != 1:
                    a = 1
                    print("a:",a)
                    #print("k=",k)
                    #print("j=",j)
                    print("11")

                # Left
                elif (round(Y[k1][0],3) > round(Y[k2][2],3)) and a != 2:
                    a = 2
                    print("a:", a)
                    #print("k=", k)
                    #print("j=", j)
                    print("22")

                # Up
                elif (round(Y[k1][3],3) > round(Y[k2][1],3)) and a != 3:
                    a = 3
                    print("a:", a)
                    #print("k=", k)
                    #print("j=", j)
                    print("33")

                # Down
                elif round(Y[k1][1],3) < round(Y[k2][3],3) and a != 4:
                    a = 4
                    print("a:", a)
                    #print("k=", k)
                    #print("j=", j)
                    print("44")

                #print("bingo:", a)
                #print("k:", k)
                while k==[0,1]:
                    self.brick1.update(a, None, None)
                    self.brick2.update(a, None, None)
                    print("A1")
                    break
                while k==[0,2]:
                    self.brick1.update(a, None, None)
                    self.brick3.update(a, None, None)
                    print("A2")
                    break
                while k==[0,3]:
                    self.brick1.update(a, None, None)
                    self.brick4.update(a, None, None)
                    print("A3")
                    break
                while k==[0,4]:
                    self.brick1.update(a, None, None)
                    self.brick4.update(a, None, None)
                    print("A4")
                    break
                while k==[1,2]:
                    self.brick2.update(a, None, None)
                    self.brick3.update(a, None, None)
                    print("A5")
                    break
                while k==[1,3]:
                    self.brick2.update(a, None, None)
                    self.brick4.update(a, None, None)
                    print("A6")
                    break
                while k==[1,4]:
                    self.brick2.update(a, None, None)
                    self.brick5.update(a, None, None)
                    print("A7")
                    break
                while k==[2,3]:
                    self.brick3.update(a, None, None)
                    self.brick4.update(a, None, None)
                    print("A8")
                    break
                while k==[2,4]:
                    self.brick3.update(a, None, None)
                    self.brick5.update(a, None, None)
                    print("A9")
                    break
                break
            #a = 0

    def click_check(self):
        self.canvas.bind('<ButtonPress-1>', self.callback)
        tags = self.canvas.find_all()
        X1=[]
        Y1=[]
        counter =0
        for tag in tags:
            x0, y0, x1, y1 = self.canvas.coords(tag)
            center_x = (x0 + x1) / 2
            center_y = (y0 + y1) / 2
            #X1.append(center)
            coords2 = [x0, y0, x1, y1]
            Y1.append(coords2)
            counter +=1
            while self.mouse_x >= x0 and self.mouse_x <= x1 and self.mouse_y >= y0 and self.mouse_y <= y1:
                print("mouse")
                print(type(center_x))
                x_move = (center_x - self.mouse_x)
                y_move = (center_y - self.mouse_y )
                a = 5
                if counter == 1:
                    print("a1")
                    self.brick1.update(a,x_move,y_move)

                elif counter == 2:
                    print("a2")
                    self.brick2.update(a,x_move,y_move)
                    counter = 0
                elif counter == 3:
                    print("a3")
                    self.brick3.update(a, x_move,y_move)
                elif counter == 4:
                    self.brick4.update(a,x_move,y_move)
                elif counter == 5:
                    self.brick5.update(a,x_move,y_move)
                self.mouse_x = 0
                self.mouse_y = 0
                break

            #print("X1:",X1)



class GameObject(object):
    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item




    def get_position(self):
        return self.canvas.coords(self.item)

    def move(self, x, y):
        self.canvas.move(self.item, x, y)


class Brick(GameObject):

    def __init__(self, canvas, d, h, xVelocity, yVelocity, color):
        self.width = 30
        self.height = 30
        self.gravity = 0.7
        self.friction = 0.5
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

        item = canvas.create_oval(d - self.width,
                                  h - self.height,
                                  d + self.width,
                                  h + self.height,
                                  fill=color, tags='ball')

        super(Brick, self).__init__(canvas, item)

    def update(self, a,center_x,center_y):

        coords = self.get_position()
        if coords[3] >= 500 and self.yVelocity < 0.1:
            self.xVelocity = 0
            self.yVelocity = 0
            self.friction = 0
            self.gravity = 0
            print("1")

        if (coords[3] >= 500 or coords[1] < 0 or a == 3 or a == 4):
            self.yVelocity *= -1
            print("2")

        if (coords[2] >= 500 or coords[0] <= 0 or a == 1 or a == 2):
            print("3")
            self.xVelocity = -(self.xVelocity * self.friction)
            #print("xVeelocity", self.xVelocity)
        if a ==5:
            print("centerx:",center_x)
            print("centery:", center_y)
            self.xVelocity =center_x
            self.yVelocity = center_y
            a=0

        self.yVelocity += self.gravity
        print("xVelo:", self.xVelocity)
        print("yVelo:", self.yVelocity)
        self.move(self.xVelocity, self.yVelocity)
        #print("move3:", self.xVelocity, self.yVelocity)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Bouncing Ball")
    game = Game(root)

    game.mainloop()
    while True:
        print("asd")
