from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import filedialog
   
"""  Necessary Function """    
#FUNCTION BUKA FILE
def buka():
    global imgInput
    window.filename = filedialog.askopenfilename(initialdir="C:\Debin\Kuliah\.Tugas\Semester 3\Pengolahan Citra Digital - C", title="Select File", filetypes=(("png files", "*.png"),("all files", "*.*")))
    alamatFile = window.filename
    
    #TEMPAT FOTO YANG DI UPLOAD
    if alamatFile:
        imgInput = Image.open(alamatFile).resize(imageSize)
        bukafoto["image"] = ImageTk.PhotoImage(imgInput)
        labelInput.configure(image=bukafoto["image"])


# FUNCTION COPY IMAGE
def copy(): 
    #input warna
    for xpos in range(imgInput.width):
        for ypos in range(imgInput.height):
            rbuf = imgInput.getpixel((xpos,ypos))[0]
            gbuf = imgInput.getpixel((xpos,ypos))[1]
            bbuf = imgInput.getpixel((xpos,ypos))[2]
            imageData.append([xpos, ypos, rbuf,gbuf,bbuf])
            # data[x,y] = (r,g,b)

    for data in imageData:
        x,y,r,g,b = data
        datafoto[x,y] = (r,g,b)
    # print(gbuf, type(gbuf))
    # imgcopy.show()
    # print(imageData[100])
    
    copyfoto["image"] = ImageTk.PhotoImage(imgcopy)
    labelCopy.configure(image=copyfoto["image"])
    labelCopy.image=copyfoto["image"]
    
#function RGB
def my_update():
    option = var.get()
    #option
    if option == 1: #red
        for data in imageData:
            x,y,r,g,b = data
            dataRGB[x,y] = (r,0,0)
    elif option == 2: #green
        for data in imageData:
            x,y,r,g,b = data
            dataRGB[x,y] = (0,g,0)
    elif option == 3: #blue
        for data in imageData:
            x,y,r,g,b = data
            dataRGB[x,y] = (0,0,b)
    elif option == 4: #cyan
        for data in imageData:
            x,y,r,g,b = data
            dataRGB[x,y] = (0,g,b)
    elif option == 5: #magenta
        for data in imageData:
            x,y,r,g,b = data
            dataRGB[x,y] = (r,0,b)
    elif option == 6: #yellow
        for data in imageData:
            x,y,r,g,b = data
            dataRGB[x,y] = (r,g,0)

    #TEMPAT FOTO UBAH RGB
    gambarRgb["image"] = ImageTk.PhotoImage(imgRgb)
    labelRgb.configure(image=gambarRgb["image"])
    labelRgb.image = gambarRgb["image"]

#restart
def restart():
    print(type(imageData))
    imageInput = Image.new("RGB", imageSize) 
    bukafoto['image'] = ImageTk.PhotoImage(imageInput)
    labelInput.configure(image=bukafoto["image"])
    
    copyfoto["image"] = ImageTk.PhotoImage(imageInput)
    labelCopy.configure(image=copyfoto["image"])
    labelCopy.image=copyfoto["image"]
    
    gambarRgb["image"] = ImageTk.PhotoImage(imageInput)
    labelRgb.configure(image=gambarRgb["image"])
    labelRgb.image = gambarRgb["image"]
    
    
""" Necessary Variable """
#var size
imageSize = (150,250)
#array data
imageData = []
#DICT VAR
bukafoto, copyfoto, gambarRgb = dict(), dict(), dict()#biar foto ga ke garbage collected


""" Start Tkinter Window """
window = Tk()
window.resizable(0,0)

#FRAME
frameGambarInput = Frame(window)
frameGambarCopy = Frame(window)
frameGambarRgb = Frame(window)

"""DEKLARASI IMAGE KOSONG"""
#input
imageInput = Image.new("RGB", imageSize)         
bukafoto['image'] = ImageTk.PhotoImage(imageInput)              
labelInput = Label(frameGambarInput, image=bukafoto["image"])
labelInput.pack()

#copy
imgcopy = Image.new("RGB", imageSize)
datafoto = imgcopy.load()
copyfoto['image'] = ImageTk.PhotoImage(imgcopy)
labelCopy = Label(frameGambarCopy, image=copyfoto["image"])
labelCopy.pack()

#rgb value
imgRgb = Image.new("RGB", imageSize)
dataRGB = imgRgb.load()
gambarRgb['image'] = ImageTk.PhotoImage(imgRgb)
labelRgb = Label(frameGambarRgb, image=gambarRgb['image'])
labelRgb.pack()
        
""" Necessary Button """        
#BUTTON BUKA FILE
selectFileButton = Button(window, text="Open Files", command=buka)
copyFileButton = Button(window, text="Copy", command=copy)
resetFileButton = Button(window, text="Reset", command=restart)

#var radiobutton
var = IntVar()

#CHECK BOX RGB CMY
warnaRed = ttk.Radiobutton(window, text= "RED", variable=var, value=1, command=my_update)
warnaGreen = ttk.Radiobutton(window, text= "GREEN", variable=var, value=2, command=my_update)
warnaBlue = ttk.Radiobutton(window, text= "BLUE", variable=var, value=3, command=my_update)
warnaCyan = ttk.Radiobutton(window, text= "CYAN", variable=var, value=4, command=my_update)
warnaMagenta = ttk.Radiobutton(window, text= "MAGENTA", variable=var, value=5, command=my_update)
warnaYellow = ttk.Radiobutton(window, text= "YELLOW", variable=var, value=6, command=my_update)

#GRID FRAME
frameGambarInput.grid(row = 1, column = 1, columnspan = 2, sticky = W, padx=1)
frameGambarCopy.grid(row = 1, column = 3, columnspan = 4, sticky = W)
frameGambarRgb.grid(row = 1, column = 5, columnspan = 6, sticky = W)

#GRID BUTTON
selectFileButton.grid(row=4, column=1,sticky=EW)
copyFileButton.grid(row=4, column=2,sticky=EW)
resetFileButton.grid(row=4, column=3,sticky=NSEW)

#GRID CHECKBOX
warnaRed.grid(row=2, column=5,sticky=EW)
warnaGreen.grid(row=3, column=5,sticky=EW)
warnaBlue.grid(row=4, column=5,sticky=EW)
warnaCyan.grid(row=2, column=6,sticky=EW)
warnaMagenta.grid(row=3, column=6,sticky=EW)
warnaYellow.grid(row=4, column=6,sticky=EW)

#GRID KOSONG
labelKosong1 = Label(window, text="                                    ")
labelKosong1.grid(row=2, column=4,sticky=NSEW, padx=1)

window.mainloop()