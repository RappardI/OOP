import tkinter
root = tkinter.Tk()
root.resizable(False, False)
myCanvas = tkinter.Canvas(root, bg="white", height=600, width=800)
shape1 = myCanvas.create_rectangle(20, 20, 100, 100, fill="blue")
#initialize the constants xx, yy
xx =yy = 3
shape2 = myCanvas.create_rectangle(20, 20, 100, 100, fill="red")
xx1 =yy1 = 7
def move_shape():
    global xx, yy
    #move the shape with the constant xx, yy
    myCanvas.move(shape1, xx, yy)
    #get the current coordinates of the shape
    (x1, y1, x2, y2) = myCanvas.coords(shape1)
    #check the boundaries of the coordinates and change the constants xx, yy
    if x1 <= 0 or x2 >= 800:
        xx = -xx
    if y1 <= 0 or y2 >= 600:
        yy = -yy

    global xx1, yy1
    myCanvas.move(shape2, xx1, yy1)
    (x1, y1, x2, y2) = myCanvas.coords(shape2)
    if x1 <= 0 or x2 >= 800:
        xx1 = -xx1
    if y1 <= 0 or y2 >= 600:
        yy1 = -yy1

    myCanvas.after(30, move_shape)

   if shape

#in the main program call the function move_shape()
myCanvas.after(30,move_shape())
myCanvas.pack()
root.mainloop()