# import Tkinter

# top = Tkinter.Tk()

# C = Tkinter.canvas(top, bg="blue", height = 250, width = 300)

# coord = 10, 50, 240, 210

# arc = C.create_arc(Coord, start=0, extent=150, fill="red")

# C.pack()
# top.mainloop()

from tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Shapes")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        # the hanging thing
        canvas.create_line(250, 15, 250, 300)
        canvas.create_line(110, 15, 110, 65)
        canvas.create_line(110, 15, 250, 15)
        canvas.create_line(230, 300, 270, 300)
        # head
        canvas.create_oval(75, 65, 150, 140, outline="black",
            width=1)
        # body
        canvas.create_line(110, 140, 110, 240)
        # left arm
        canvas.create_line(35, 135, 110, 190)
        # right arm
        canvas.create_line(185, 135, 110, 190)
        # left leg
        canvas.create_line(35, 295, 110, 240)
        # right leg
        canvas.create_line(185, 295, 110, 240)

        canvas.pack(fill=BOTH, expand=1)
        # canvas.create_oval(110, 10, 210, 80, outline="#f11",
        #     fill="#1f1", width=2)
        # canvas.create_rectangle(230, 10, 290, 60,
        #     outline="#f11", fill="#1f1", width=2)
        # canvas.create_arc(30, 200, 90, 100, start=0,
        #     extent=210, outline="#f11", fill="#1f1", width=2)

        # points = [150, 100, 200, 120, 240, 180, 210,
        #     200, 150, 150, 100, 200]
        # canvas.create_polygon(points, outline='#f11',
        #     fill='#1f1', width=2)

        canvas.pack(fill=BOTH, expand=1)


def main():

    root = Tk()
    ex = Example()
    root.geometry("500x500+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()