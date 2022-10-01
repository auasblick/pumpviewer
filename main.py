import tkinter as tkr
from tkinter.ttk import *
# import matplotlib as mp
import numpy as np
from tkinter import messagebox as mb
import positioning as pos
import generationing as gen
import png #debug
from PIL import ImageTk, Image

# important globals:
# app; screen_width; screen_height; w_width; w_height; color; task;
app = tkr.Tk()
app.configure(background="white")
app.wm_iconbitmap('ujams_icon.ico')
screen_width = int(app.winfo_screenwidth())
screen_height = int(app.winfo_screenheight())
w_width = app.winfo_width()
w_height = app.winfo_height()
color = ["white", "black", "white smoke", "dodger blue", "light"]
task = "view"

# geninfo = gen.GenerateCollection()

# Define window size
app.title("UJAMS Pump Curve Modification Tool")
app.geometry("{}x{}+{}+{}".format(round(screen_width*0.75), round(screen_height*0.75), round(screen_width/8),
                                  round(screen_height/8)))
app.minsize(200, 200)


# change visual appearance
def vischange():
    global color
    if color[4] == "light":
        color = ["black", "white", "gray10", "darkorange1", "dark"]
    else:
        color = ["white", "black", "white smoke", "dodger blue", "light"]
    colorchange()


def colorchange():
    global color
    global task
    if task == "view":
        app.configure(background=color[0])
        plot_canvas.config(bg=color[0], highlightbackground=color[2])
        pumpone_canvas.config(bg=color[0], highlightbackground=color[2])
        pumptwo_canvas.config(bg=color[0], highlightbackground=color[2])
        uob.configure(bg=color[0], fg=color[1], activebackground=color[3], activeforeground=color[0])
        cob.configure(bg=color[0], fg=color[1], activebackground=color[3], activeforeground=color[0])
    elif task == "generate":
        app.configure(background=color[0])
        gen_overview_canvas.config(bg=color[0], highlightbackground=color[2])
        gen_settings_canvas.config(bg=color[0], highlightbackground=color[2])
        gen_draw_canvas.config(bg=color[0], highlightbackground=color[2])
        gen_addsource.configure(bg=color[0], fg=color[1], activebackground=color[3], activeforeground=color[0])


def resize():
    global w_width
    global w_height
    if (not w_width == app.winfo_width()) | (not w_height == app.winfo_height()):
        global task
        w_width = app.winfo_width()
        w_height = app.winfo_height()

        # call function to resize the buttons
        if task == "view":
            resize_view(w_width, w_height)
        elif task == "generate":
            resize_generate(w_width, w_height)
        elif task == "modify":
            resize_modify(w_width, w_height)

    app.after(10, resize)


def callview():
    global task
    global w_width
    global w_height
    if task == "generate":
        forgetgenerate()
    elif task == "modify":
        forgetmodify()
    task = "view"
    resize_view(w_width, w_height)


def callgenerate():
    global task
    global w_width
    global w_height
    if task == "view":
        forgetview()
    elif task == "modify":
        forgetmodify()
    task = "generate"
    resize_generate(w_width, w_height)


def callmodify():
    global task
    global w_width
    global w_height
    if task == "view":
        forgetview()
    elif task == "generate":
        forgetgenerate()
    task = "modify"
    resize_modify(w_width, w_height)


def resize_view(width, height):
    xop, yop, xlp, ylp, xopo, yopo, xlpo, ylpo, xopt, yopt, xlpt, ylpt = pos.raw_view_position(width, height)
    plot_canvas.config(width=xlp, height=ylp)
    plot_canvas.place(x=xop, y=yop)

    pumpone_canvas.config(width=xlpo, height=ylpo)
    pumpone_canvas.place(x=xopo, y=yopo)

    pumptwo_canvas.config(width=xlpt, height=ylpt)
    pumptwo_canvas.place(x=xopt, y=yopt)

    uob.place(x=xopo+10, y=yopo+10)
    cob.place(x=xopo+110, y=yopo+10)

    colorchange()


def resize_generate(width, height):
    xp1, yp1, xl1, yl1, xp2, yp2, xl2, yl2, xp3, yp3, xl3, yl3 = pos.raw_generate_position(width, height, [3, 2])
    gen_overview_canvas.config(width=xl1, height=yl1)
    gen_overview_canvas.place(x=xp1, y=yp1)

    gen_settings_canvas.config(width=xl2, height=yl2)
    gen_settings_canvas.place(x=xp2, y=yp2)

    gen_draw_canvas.config(width=xl3, height=yl3)
    gen_draw_canvas.place(x=xp3, y=yp3)

    gen_addsource.place(x=xp1 + 10, y=yp1 + 10)

    gen_import_img.config(width=xl3-20, height=yl3-20)
    gen_import_img.place(x=xp3+10, y=yp3+10)

    colorchange()


def resize_modify(width, height):
    print("resize modificator")


def forgetview():
    uob.place_forget()
    cob.place_forget()
    plot_canvas.place_forget()
    pumpone_canvas.place_forget()
    pumptwo_canvas.place_forget()
    print("View forgotten")


def forgetgenerate():
    # canvas
    gen_overview_canvas.place_forget()
    gen_settings_canvas.place_forget()
    gen_draw_canvas.place_forget()
    # buttons
    gen_addsource.place_forget()
    # frames
    gen_import_img.place_forget()
    print("Generate forgotten")


def forgetmodify():
    print("Hide modify lables")


def donothing():
    mb.showerror("Marko's Freundin", "Laura ist das hübscheste Mädchen der Welt", parent=app)


def fuckyou():
    print("fuck you")


# add menubar
menubar = tkr.Menu(app)
filemenu = tkr.Menu(menubar, tearoff=0)
filemenu.add_command(label="Import Pump Collection", command=donothing)
filemenu.add_command(label="UJAMS Pump Viewer", command=callview)
filemenu.add_command(label="Create New Pump Collection", command=callgenerate)
filemenu.add_command(label="Modify Pump Collection", command=callmodify)
menubar.add_cascade(label="File", menu=filemenu)

settmenu = tkr.Menu(menubar, tearoff=0)
settmenu.add_command(label="Dark Mode", command=vischange)
settmenu.add_command(label="Change Colors", command=donothing)
menubar.add_cascade(label="Settings", menu=settmenu)

helpmenu = tkr.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Fuck you", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

app.config(menu=menubar)

# canvas
# view
plot_canvas = tkr.Canvas(app)
pumpone_canvas = tkr.Canvas(app)
pumptwo_canvas = tkr.Canvas(app)
# generate
gen_overview_canvas = tkr.Canvas(app)
gen_draw_canvas = tkr.Canvas(app)
gen_settings_canvas = tkr.Canvas(app)
# modify


# add main buttons
# viewer buttons
uob = tkr.Button(app, width=10, height=1, text="Update", command=donothing)
cob = tkr.Button(app, width=10, height=1, text="Clear", command=fuckyou)
# generate buttons
gen_addsource = tkr.Button(app, width=10, height=1, text="plusone", command=gen.import_source)


# dummy image
gen_import_img = Frame(app, style='My.TFrame', height=70, width=400)
img_loc = "C:/Users/Marko/Documents/UJAMS/Feed Pumps/pdfattempt/Amarex_KRT_F__n_3500_1750_rpm.png"
reader = png.Reader(filename=img_loc)
img_w, img_h, img_arr, z = reader.read_flat()
img_rgb = np.zeros([img_h, img_w, 3], np.uint8)
c = 0
for u in range(img_rgb.shape[0]):
    for v in range(img_rgb.shape[1]):
        img_rgb[u, v, 0:3] = img_arr[c:c+3]
        c += 3
img = Image.fromarray(img_rgb, "RGB")
img.show()
imgtk = ImageTk.PhotoImage(img)
label = Label(gen_import_img, image=imgtk)

# run
resize()
app.mainloop()
