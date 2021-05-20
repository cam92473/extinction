import tkinter as tk
from PIL import Image, ImageTk
import ctypes
import tkinter.messagebox

class Window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Extinction")
        self.geometry("1400x700+350+150")
        self.configure()

def get_image(filepath,dimx,dimy):
    image = Image.open(f"{filepath}")
    image_rsize = image.resize((dimx,dimy))
    image_rsize_conv = ImageTk.PhotoImage(image_rsize)
    return image_rsize_conv

def create_widgets(mwin,tk):

    ### Resolution
    ctypes.windll.shcore.SetProcessDpiAwareness(1)

    ### Parameter boxes
    paramlab1 = tk.Label(mwin,font=("Arial",10),text = "c1")
    paramlab1.grid(row=2, column=3)
    parambox1 = tk.Entry(mwin,font=("Arial",10))
    parambox1.insert(0,"-0.175")
    parambox1.grid(row=2,column=4)

    paramlab2 = tk.Label(mwin,font=("Arial",10),text = "c2")
    paramlab2.grid(row=3, column=3)
    parambox2 = tk.Entry(mwin,font=("Arial",10))
    parambox2.insert(0,"0.807")
    parambox2.grid(row=3,column=4)

    paramlab3 = tk.Label(mwin,font=("Arial",10),text = "c4")
    paramlab3.grid(row=4, column=3)
    parambox3 = tk.Entry(mwin,font=("Arial",10))
    parambox3.insert(0,"0.319")
    parambox3.grid(row=4,column=4)

    paramlab5 = tk.Label(mwin,font=("Arial",10),text = "x0")
    paramlab5.grid(row=6, column=3)
    parambox5 = tk.Entry(mwin,font=("Arial",10))
    parambox5.insert(0,"4.592")
    parambox5.grid(row=6,column=4)

    paramlab6 = tk.Label(mwin,font=("Arial",10),text = "c3")
    paramlab6.grid(row=7, column=3)
    parambox6 = tk.Entry(mwin,font=("Arial",10))
    parambox6.insert(0,"2.991")
    parambox6.grid(row=7,column=4)

    paramlab7 = tk.Label(mwin,font=("Arial",10),text = "gamma")
    paramlab7.grid(row=8, column=3)
    parambox7 = tk.Entry(mwin,font=("Arial",10))
    parambox7.insert(0,"0.922")
    parambox7.grid(row=8,column=4)

    paramlab8 = tk.Label(mwin,font=("Arial",10),text = "O3")
    paramlab8.grid(row=9, column=3)
    parambox8 = tk.Entry(mwin,font=("Arial",10))
    parambox8.insert(0,"0.000")
    parambox8.grid(row=9,column=4)

    paramlab9 = tk.Label(mwin,font=("Arial",10),text = "O2")
    paramlab9.grid(row=10, column=3)
    parambox9 = tk.Entry(mwin,font=("Arial",10))
    parambox9.insert(0,"1.322")
    parambox9.grid(row=10,column=4)

    paramlab10 = tk.Label(mwin,font=("Arial",10),text = "O1")
    paramlab10.grid(row=11, column=3)
    parambox10 = tk.Entry(mwin,font=("Arial",10))
    parambox10.insert(0,"2.055")
    parambox10.grid(row=11,column=4)

    paramlab11 = tk.Label(mwin,font=("Arial",10),text = "k_IR")
    paramlab11.grid(row=12, column=3)
    parambox11 = tk.Entry(mwin,font=("Arial",10))
    parambox11.insert(0,"1.057")
    parambox11.grid(row=12,column=4)

    paramlab12 = tk.Label(mwin,font=("Arial",10),text = "R_V")
    paramlab12.grid(row=13, column=3)
    parambox12 = tk.Entry(mwin,font=("Arial",10))
    parambox12.insert(0,"3.001")
    parambox12.grid(row=13,column=4)

    toplabel = tk.Label(mwin,font=("Arial",12),text="Parameters").grid(row=1,column=4)

    ### Central Image
    photo1 = get_image('extinction_curve.PNG', 515, 310)
    mwin.photo = photo1
    imglabel = tk.Label(mwin, image=photo1).grid(row=3,column=7, rowspan = 8,columnspan=10,sticky=tk.W)

    ### Sliders and c5
    sliderpos1 = tk.IntVar()
    sliderpos2 = tk.IntVar()
    sliderpos3 = tk.IntVar()

    slider1 = tk.Scale(mwin, from_=500, to=1500, orient=tk.HORIZONTAL, length = 200, variable = sliderpos1)
    slider1.set(1000)
    slider1.grid(row=3, column=19)
    slider2 = tk.Scale(mwin, from_=1, to=1000, orient=tk.HORIZONTAL, length = 200, variable = sliderpos2)
    slider2.set(270)
    slider2.grid(row=6, column=19)
    slider3 = tk.Scale(mwin, from_=1, to=1000, orient=tk.HORIZONTAL, length = 200, variable = sliderpos3)
    slider3.set(164)
    slider3.config(state = tk.DISABLED)
    slider3.grid(row=9, column=19)

    textobj1 = tk.StringVar()
    textobj2 = tk.StringVar()
    textobj3 = tk.StringVar()

    def getsliderval1():
        textobj1.set(str(round(1000/sliderpos1.get(),4)))

    def getsliderval2():
        textobj2.set(str(round(1000/sliderpos2.get(),4)))

    def getsliderval3():
        textobj3.set(str(round(1000/sliderpos3.get(),4)))

    def getc5(useless):
        try:
            slider3.config(state=tk.NORMAL)
            slider3.set(round(1000/float(parambox4.get()),6))
            slider3.config(state = tk.DISABLED)
        except:
            pass

    conv_button1 = tk.Button(mwin,text="inv. μm",bd=3,command = getsliderval1)
    conv_button1.grid(row=3,column=21)
    conv_label1 = tk.Label(mwin, width = 10, bg = "snow", borderwidth=1, relief = tk.SOLID, textvariable = textobj1, pady = 4)
    conv_label1.grid(row = 3,column = 23)
    abovelabel1 = tk.Label(mwin,text="Infrared/Optical Boundary [nm]")
    abovelabel1.grid(row=2,column=19)

    conv_button2 = tk.Button(mwin,text="inv. μm",bd=3,command = getsliderval2)
    conv_button2.grid(row=6,column=21)
    conv_label2 = tk.Label(mwin, width = 10, bg = "snow", borderwidth=1, relief = tk.SOLID, textvariable = textobj2, pady = 4)
    conv_label2.grid(row = 6,column = 23)
    abovelabel2 = tk.Label(mwin,text="Optical/Near UV Boundary [nm]")
    abovelabel2.grid(row=5,column=19)

    conv_button3 = tk.Button(mwin,text="inv. μm",bd=3,command = getsliderval3)
    conv_button3.grid(row=9,column=21)
    conv_label3 = tk.Label(mwin, width = 10, bg = "snow", borderwidth=1, relief = tk.SOLID, textvariable = textobj3, pady = 4)
    conv_label3.grid(row = 9,column = 23)
    abovelabel3 = tk.Label(mwin,text="Near UV/Far UV Boundary [nm]")
    abovelabel3.grid(row=8,column=19)

    paramlab4 = tk.Label(mwin,font=("Arial",10),text = "c5")
    paramlab4.grid(row=5, column=3)
    parambox4 = tk.Entry(mwin,font=("Arial",10))
    parambox4.bind('<Return>', getc5)
    parambox4.insert(0,"6.097")
    parambox4.grid(row=5,column=4)

    explainlab = tk.Label(mwin, font = ("Arial",8), text="*change c5 to move this slider")
    explainlab.grid(row=10, column=21, columnspan = 3)

    ### Checkboxes

    chk1 = tk.IntVar()
    chk2 = tk.IntVar()
    chk3 = tk.IntVar()

    printout = tk.Checkbutton(mwin,text="Create output file",font=("Arial",10),variable=chk1)
    printout.grid(row = 11, column = 19, sticky = tk.W)
    printout.select()
    scatter = tk.Checkbutton(mwin, text = "Create scatter plot of data",font=("Arial",10),variable=chk2)
    scatter.grid(row=12, column=19,sticky = tk.W)
    scatter.select()
    curve = tk.Checkbutton(mwin, text = "Create plot of full extinction curve",font=("Arial",10),variable=chk3)
    curve.grid(row=13, column=19,sticky = tk.W)
    curve.select()

    ### Help, Reset and Start

    def thegreatreset():
        parambox1.delete(0,20)
        parambox1.insert(0, "-0.175")
        parambox2.delete(0,20)
        parambox2.insert(0, "0.807")
        parambox3.delete(0,20)
        parambox3.insert(0, "0.319")
        parambox4.delete(0,20)
        parambox4.insert(0, "6.097")
        parambox5.delete(0,20)
        parambox5.insert(0, "4.592")
        parambox6.delete(0,20)
        parambox6.insert(0, "2.991")
        parambox7.delete(0,20)
        parambox7.insert(0, "0.922")
        parambox8.delete(0,20)
        parambox8.insert(0, "0.000")
        parambox9.delete(0,20)
        parambox9.insert(0, "1.322")
        parambox10.delete(0,20)
        parambox10.insert(0, "2.055")
        parambox11.delete(0,20)
        parambox11.insert(0, "1.057")
        parambox12.delete(0,20)
        parambox12.insert(0, "3.001")

        slider1.set(1000)
        slider2.set(270)
        slider3.set(164)

        getsliderval1()
        getsliderval2()
        getsliderval3()

        printout.select()
        scatter.deselect()
        curve.deselect()


    def openhelp():
        helpmessage = tk.messagebox.showinfo("Help"," Press Start to calculate a new extinction curve based on the parameters and region boundaries chosen. This extinction curve is used to find the outputs to the wavelengths (in nm) inputted in the wavelengths.csv file. \n\n Use the checkboxes to display the points on the extinction curve where the data lie, show the entire extinction curve, or create a new csv with the corresponding output to each wavelength. \n\n The sliders control the connection points for the various pieces of the extinction curve. For example, the cubic spline will extend from the IR/Opt boundary to the Opt/Near UV boundary and pass through the optical filter values specified by the O3, O2 and O1 parameters. These optical filter points are at 553 nm, 400 nm and 330 nm.\n\n To learn more about the extinction curve and how the parameters affect its shape, see the html file in the same folder as this program.\n\nNote: if there is a slight descrepency between the displayed c5 values, the entered c5 value on the left will be used.")

    def getinfoclose(mwin, tk):

        try:
            user_c1 = float(parambox1.get())
            user_c2 = float(parambox2.get())
            user_c4 = float(parambox3.get())
            user_c5 = float(parambox4.get())
            user_x0 = float(parambox5.get())
            user_c3 = float(parambox6.get())
            user_gamma = float(parambox7.get())
            user_O3 = float(parambox8.get())
            user_O2 = float(parambox9.get())
            user_O1 = float(parambox10.get())
            user_k_IR = float(parambox11.get())
            user_R_V = float(parambox12.get())
            user_ir_shrtst = slider1.get()
            user_opt_shrtst = slider2.get()
            user_uvN_shrtst = slider3.get()
            user_createoutput = chk1.get()
            user_scatter = chk2.get()
            user_fullplot = chk3.get()

        except:
            tk.messagebox.showinfo('Error', 'Invalid input.\n\nTry:\n\n1) Checking that the IR/Optical boundary is at a longer wavelength than the Optical/Near UV boundary \n\n2) Checking that the Near UV/Far UV boundary slider is properly coordinated with the c5 parameter by hitting ENTER after typing in c5')
        else:
            if  user_ir_shrtst < user_opt_shrtst:
                tk.messagebox.showinfo('Error', 'Invalid input.\n\nTry:\n\n1) Checking that the IR/Optical boundary is at a longer wavelength than the Optical/Near UV boundary \n\n2) Checking that the Near UV/Far UV boundary slider is properly coordinated with the c5 parameter by hitting ENTER after typing in c5')
            elif (user_c5 - user_uvN_shrtst) > abs(.1):
                tk.messagebox.showinfo('Error', 'Invalid input.\n\nTry:\n\n1) Checking that the IR/Optical boundary is at a longer wavelength than the Optical/Near UV boundary \n\n2) Checking that the Near UV/Far UV boundary slider is properly coordinated with the c5 parameter by hitting ENTER after typing in c5')
            else:
                mwin.destroy()
                mwin.setvar(name="user_c1", value=user_c1)
                mwin.setvar(name="user_c2", value=user_c2)
                mwin.setvar(name="user_c4", value=user_c4)
                mwin.setvar(name="user_c5", value=user_c5)
                mwin.setvar(name="user_x0", value=user_x0)
                mwin.setvar(name="user_c3", value=user_c3)
                mwin.setvar(name="user_gamma", value=user_gamma)
                mwin.setvar(name="user_O3", value=user_O3)
                mwin.setvar(name="user_O2", value=user_O2)
                mwin.setvar(name="user_O1", value=user_O1)
                mwin.setvar(name="user_k_IR", value=user_k_IR)
                mwin.setvar(name="user_R_V", value=user_R_V)
                mwin.setvar(name="user_ir_shrtst", value=user_ir_shrtst)
                mwin.setvar(name="user_opt_shrtst", value=user_opt_shrtst)
                mwin.setvar(name="user_uvN_shrtst", value=user_uvN_shrtst)
                mwin.setvar(name="user_createoutput", value=user_createoutput)
                mwin.setvar(name="user_scatter", value=user_scatter)
                mwin.setvar(name="user_fullplot", value=user_fullplot)


    reset = tk.Button(mwin,text="Reset",font=("Arial",14),bd=4,command=thegreatreset,padx=20,pady=8)
    reset.grid(row=11,column=8,rowspan=3)
    help = tk.Button(mwin, text="Help",font=("Arial",14),bd=4, command = openhelp,padx=25,pady=8)
    help.grid(row=11, column=11,rowspan=3)
    start = tk.Button(mwin, text = "Start",font=("Arial",14),bd=4, command = lambda:getinfoclose(mwin, tk),padx=25,pady=8)
    start.grid(row=11, column=14,rowspan=3)


def configure_grid(mwin, grid_rc):
    for row in range(0,len(grid_rc[0])):
        mwin.rowconfigure(row,minsize=grid_rc[0][row])
    for column in range(0,len(grid_rc[1])):
        mwin.columnconfigure(column,minsize=grid_rc[1][column])