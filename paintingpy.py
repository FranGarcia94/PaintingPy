#============================= PaintingPy =============================#
#                                                                      #
#                    Simple GUI to paint with Python                   #
#                                                                      #
#                                                     @FranGarcia94    #
#======================================================================#


from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import messagebox as MessageBox
from random import *
from tkinter.ttk import Separator
from PIL import Image, ImageDraw


def choose_color():

    global color
    color = askcolor()
    color_button.config(bg = color[1])



def outline_color():

    global color_outline
    color_outline = askcolor()
    color_outline_button.config(bg = color_outline[1])



def paint( event ):
    global cl

    if opVar.get() == 0: # Oval

        cl=[]
        x1, y1 = ( event.x - scaleVar.get() ), ( event.y - scaleVar.get() )
        x2, y2 = ( event.x + scaleVar.get() ), ( event.y + scaleVar.get() )

        if fillVar.get() == 0:

            w.create_oval( x1, y1, x2, y2, fill = color[1], outline = color_outline[1])
            draw.ellipse([x1, y1, x2, y2], fill = color[0], outline = color_outline[0])
        else:

            w.create_oval( x1, y1, x2, y2, fill = None, outline = color_outline[1])
            draw.ellipse([x1, y1, x2, y2], fill = None, outline = color_outline[0])        
    elif opVar.get() == 1: # Line

        cl=[]
        x1, y1 = ( event.x - scaleVar.get() ), ( event.y - scaleVar.get() )
        x2, y2 = ( event.x + scaleVar.get() ), ( event.y + scaleVar.get() )

        w.create_line(x1, y1, x2, y2, fill = color[1])
        draw.line([x1, y1, x2, y2], fill=color[0],  width=scaleVar.get())
    elif opVar.get() == 2: # Square

        cl=[]
        x1, y1 = ( event.x - scaleVar.get() ), ( event.y - scaleVar.get() )
        x2, y2 = ( event.x + scaleVar.get() ), ( event.y + scaleVar.get() )

        if fillVar.get() == 0:

            w.create_rectangle( x1, y1, x2, y2, fill = color[1],outline = color_outline[1])
            draw.rectangle([x1, y1, x2, y2], fill = color[0], outline = color_outline[0])
        else:

            w.create_rectangle( x1, y1, x2, y2, fill = None,outline = color_outline[1])
            draw.rectangle([x1, y1, x2, y2], fill = None, outline = color_outline[0])
    elif opVar.get() == 3: # Polygon

        if len(cl)<4:

                cl.append(event.x)
                cl.append(event.y)

                try:
                        w.create_line(cl[0],cl[1],cl[2],cl[3], fill = color[1])
                        draw.line([cl[0],cl[1],cl[2],cl[3]], fill = color[0])
                except:
                        pass
        elif len(cl) == 4:

                w.create_line(cl[0],cl[1],cl[2],cl[3], fill = color[1])
                draw.line([cl[0],cl[1],cl[2],cl[3]], fill = color[0])

                cl = [cl[2],cl[3]]
                cl.append(event.x)
                cl.append(event.y)

                try:
                        w.create_line(cl[0],cl[1],cl[2],cl[3], fill = color[1])
                        draw.line([cl[0],cl[1],cl[2],cl[3]], fill = color[0])
                except:
                        pass
    elif opVar.get() == 4: # Star

        x1, y1 = (event.x - scaleVar.get()), (event.y)
        x2, y2 = (event.x - scaleVar.get()//4), (event.y - scaleVar.get()//4)
        x3, y3 = (event.x), (event.y - scaleVar.get())
        x4, y4 = (event.x + scaleVar.get()//4), (event.y - scaleVar.get()//4)
        x5, y5 = (event.x + scaleVar.get()), (event.y)
        x6, y6 = (event.x + scaleVar.get()//4), (event.y + scaleVar.get()//4)
        x7, y7 = (event.x), (event.y + scaleVar.get())
        x8, y8 = (event.x - scaleVar.get()//4), (event.y + scaleVar.get()//4)

        points = [x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8]

        if fillVar.get() == 0:

            w.create_polygon(points, fill = color[1], outline = color_outline[1])
            draw.polygon([x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8],fill=color[0], outline = color_outline[0])
        else:

            w.create_polygon(points, fill = '', outline = color_outline[1])
            draw.polygon([x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8], fill = None, outline = color_outline[0])
    elif opVar.get() == 5: # Random
        
        rand_num = randint(0,1)

        x1, y1 = ( event.x - scaleVar.get() ), ( event.y - scaleVar.get() )
        x2, y2 = ( event.x + scaleVar.get() ), ( event.y + scaleVar.get() )

        if fillVar.get() == 0:

            if rand_num == 0:

                rand_shape = w.create_oval( x1, y1, x2, y2, fill = color[1], outline = color_outline[1])
                draw.ellipse([x1, y1, x2, y2], fill = color[0], outline = color_outline[0])
            else:

                rand_shape = w.create_rectangle( x1, y1, x2, y2, fill = color[1], outline = color_outline[1])
        else:

            if rand_num == 0:

                rand_shape = w.create_oval( x1, y1, x2, y2, fill = None, outline = color_outline[1])
            else:

                rand_shape = w.create_rectangle( x1, y1, x2, y2, fill = None, outline = color_outline[1])

        def movement(dx, dy):

            x1_1, y1_1, x2_1, y2_1 = list(map(int, w.coords(rand_shape))) # Crea una lista con las corrdenadas pero en vez de float con int

            if (x1_1 <= 0 and dx < 0) or (x2_1 >= canvas_width and dx > 0): # Invierte desplazamiento en x cuando choca con muros verticales. Evita bug
                
                dx = -dx
            elif (y1_1 <= 0 and dy < 0) or (y2_1 >= canvas_height and dy > 0): # Invierte desplazamiento en y cuando choca con muros horizontales. Evita bug
                
                dy = -dy

            w.move(rand_shape, dx, dy)
            w.after(25, movement, dx, dy) # Se mueve cada 25 ms
            draw.ellipse([x1_1, y1_1, x2_1, y2_1], fill = color[0], outline = color_outline[0])

        movement(randint(-15, 15), randint(-15, 15)) # Se mueve x pixeles en horizontal e y en vertical


def save():
    image1.save('paintingpy_image.png')
    MessageBox.showinfo(title = 'Saved', message = 'File Saved as: paintingpy_image.png')


def clear ():
    
    w.delete(ALL)
    
    wid = image1.width
    h = image1.height

    draw.rectangle([0, 0, wid, h], fill = "white", width = 0)

    # You would normally put that on the App class
    def show_error(self, *args):
        pass
    # but this works too
    Tk.report_callback_exception = show_error



## --- MAIN --- ##
root = Tk()
root.title( "PaintingPy" )
root.iconbitmap('logo.ico')
root.resizable(False,False)


# Variables
opVar = IntVar()
scaleVar = IntVar()
fillVar = IntVar()

canvas_width = 920
canvas_height = 380

color = ((0,0,0),['#000'])
color_outline = ((0,0,0),['#000'])
cl = []

font_1 = ("Times", "14", "bold italic")
font_2 = ("Times", "12", "bold")
font_3 = ("Helvetica", "12", "bold")

# CANVAS
w = Canvas(root, width = canvas_width, height = canvas_height)
w.config(bg = '#fff')

w.pack(expand = 1, fill = 'both')

w.bind("<B1-Motion>", paint )
w.bind("<Button-1>", paint )


# Img in PIL. It is not displayed, it is used to save the image.
image1 = Image.new("RGB", (canvas_width, canvas_height), 'white')
draw = ImageDraw.Draw(image1)


## Labels and Tools
# LabelFrame 1
bg_image = PhotoImage(file = 'bg_2.png')

mylabelframe = LabelFrame(root, text = 'Tools', font=font_1)
mylabelframe.pack(fill = 'both',expand = 1, ipadx = 10, ipady = 10, padx = 8, pady = 5)

bg_label = Label(mylabelframe, image = bg_image)
bg_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)


scale = Scale(mylabelframe, variable = scaleVar, orient = 'horizontal', from_ = 0, to = 60, label = 'Brush Thickness', length = 400, repeatdelay = 500, relief = 'sunken', sliderlength = 25)
scale.grid(row = 0, column = 0, columnspan = 3)

oval_brush = Radiobutton(mylabelframe, text = 'Circle Brush', variable = opVar, value = 0, font = font_2).grid(row = 1, column = 0, sticky = 'w')
line_brush = Radiobutton(mylabelframe, text = 'Line Brush', variable = opVar, value = 1, font = font_2).grid(row = 2, column = 0, sticky ='w')
rectangle = Radiobutton(mylabelframe, text = 'Square Brush', variable = opVar, value = 2, font = font_2).grid(row = 1, column = 1, sticky = 'w')
polygon_brush = Radiobutton(mylabelframe, text = 'Polygon', variable = opVar, value = 3, font = font_2).grid(row = 2, column = 1, sticky = 'w')
star = Radiobutton(mylabelframe, text = 'Star', variable = opVar, value = 4, font = font_2).grid(row = 3, column = 0, sticky = 'w')
random_move = Radiobutton(mylabelframe, text = 'Random', variable = opVar, value = 5, font = font_2).grid(row = 3, column = 1, sticky = 'w')


# LabelFrame 2
mylabelframe2 = LabelFrame(mylabelframe, text = 'Fill  and  Outline color', font = font_1)
mylabelframe2.grid(row = 1, column = 2, rowspan = 2, ipadx = 20, pady = 10, padx = 25)

color_button = Button(mylabelframe2, width = 5)
color_button.grid(row = 0, column = 0)
color_button.config(command = choose_color, bg = color[1])

sep = Separator(mylabelframe2, orient = 'vertical').grid(row = 0, column = 1, sticky = 'ns', padx = 5)

color_outline_button = Button(mylabelframe2, width = 5)
color_outline_button.grid(row = 0, column = 2, padx = 9)
color_outline_button.config(command = outline_color, bg = color_outline[1])

fill_button = Radiobutton(mylabelframe2, text = 'Fill', variable = fillVar, value = 0, font = font_2).grid(row = 2, column = 0, sticky = 'w')
hollow_button = Radiobutton(mylabelframe2, text = 'Hollow', variable = fillVar, value = 1, font = font_2).grid(row = 3, column = 0, sticky = 'w')
##


# Save and Clear
sep_2 = Separator(mylabelframe, orient = 'vertical').grid(row = 0, column = 4, rowspan = 4,sticky = 'ns', padx = 25)

save_image = PhotoImage(file = 'save_2.png')
clear_image = PhotoImage(file = 'refresh.png')

save_button = Button(mylabelframe, text='    Save', image = save_image, compound = 'left', padx = 8,pady = 5, font = font_3)
save_button.grid(row = 1, column = 5)
save_button.config(command = save)

clear_button = Button(mylabelframe, text='    Clear', image = clear_image, compound = 'left', padx = 8, pady = 5, font = font_3)
clear_button.grid(row = 2, column = 5)
clear_button.config(command = clear)


# Logo (Optional)
image_logo = PhotoImage(file = "logo_2.png")
lim = Label(mylabelframe, image=image_logo)
lim.place(x=750, y=85)


'''If the different images don't work, try putting the full URL or just skip the images'''


root.mainloop()
