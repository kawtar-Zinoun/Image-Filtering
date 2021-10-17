from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Style
import PIL
import numpy
from matplotlib import pyplot as plt
from numpy import array
from PIL import ImageTk, Image
import cv2
from skimage import io
from skimage.util import random_noise

root = Tk()
root.title("Image filtering with OpenCv2")
root.geometry("800x500")

labelTitle = Label(root, text="Choose a filter")

# This will create style object
style = Style();

style.configure('TButton', font=
('calibri', 10, 'bold', 'underline'),
                foreground='red')

workSpaceImage = ""
myImage = ""
labImgFiltered = Label(root,  padx=1, pady=1)

def openFileDialog():
    global workSpaceImage
    global myImage
    root.filename = filedialog.askopenfilename(initialdir="lll", title="select an Image", filetypes=(("png files", "*.png"), ("all files", "*.*")))

    if root.filename:

        pic = Image.open(root.filename)
        resized = pic.resize((300, 300), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resized)
        myImage = img
        workSpaceImage = numpy.array(resized)
        labImgFiltered.configure(image=img)
        labImgFiltered.image = img


def resetImage():
    global myImage
    labImgFiltered.configure(image=myImage)
    labImgFiltered.image = myImage

def filterGaussianNoise():
    global workSpaceImage
    imgNoised = random_noise(workSpaceImage, mode='gaussian')
    imgA = PIL.Image.fromarray((imgNoised * 255).astype(numpy.uint8))
    workSpaceImage = numpy.array(imgA)
    imgTK = ImageTk.PhotoImage(imgA)
    labImgFiltered.configure(image=imgTK)
    labImgFiltered.image = imgTK

def filterGaussianDenoise():
    global workSpaceImage
    denoise = cv2.fastNlMeansDenoisingColored(workSpaceImage, None, 8, 8, 7, 21)
    workSpaceImage = denoise
    imgA = PIL.Image.fromarray(denoise)
    imgTK = ImageTk.PhotoImage(imgA)
    labImgFiltered.configure(image=imgTK)
    labImgFiltered.image = imgTK


def filterNoiseSP():
    global workSpaceImage
    imgNoised = random_noise(workSpaceImage, mode='s&p')
    imgA = PIL.Image.fromarray((imgNoised * 255).astype(numpy.uint8))
    workSpaceImage = numpy.array(imgA)
    imgTK = ImageTk.PhotoImage(imgA)
    labImgFiltered.configure(image = imgTK)
    labImgFiltered.image = imgTK

def filterMedianDenoise():
    global workSpaceImage
    imgDenoised = cv2.medianBlur(workSpaceImage,5)
    workSpaceImage = imgDenoised
    imgA = PIL.Image.fromarray(imgDenoised)
    imgTK = ImageTk.PhotoImage(imgA)
    labImgFiltered.configure(image=imgTK)
    labImgFiltered.image = imgTK


btnOpenFileDialog = Button(root, text="Choose picture", bg = '#FF7777',
                           command=openFileDialog, width=10, padx=50, pady=8)

btnFilterGaussianNoise = Button(root, text="Gaussian noise", bg='#0052cc', fg='#ffffff', padx=50, width=10, pady=7,
                                command=filterGaussianNoise)
btnFilterGaussianDenoise = Button(root, text="Gaussian denoise", bg='#0052cc', fg='#ffffff', padx=50, width=10,
                                  pady=7,  command=filterGaussianDenoise)

btnFilterNoiseSP = Button(root, text="Salt and pepper noise", bg='#0052cc', fg='#ffffff', padx=50, width=10,
                          pady=7, command=filterNoiseSP)
btnFilterMedianDenoise = Button(root, text="Median denoise", bg='#0052cc', fg='#ffffff', padx=50, width=10,
                                pady=7, command=filterMedianDenoise)
btnReset = Button(root, text="Reset", bg='#0052cc', fg='#ffffff', padx=50, width=10,
                  pady=7, command=resetImage)


labelTitle.grid(row=0, column=1)
labImgFiltered.grid(row=9, column=1, pady=(10, 10))
btnOpenFileDialog.grid(row=3, column=0, pady=(10, 10))
btnFilterGaussianNoise.grid(row=3, column=1)
btnFilterGaussianDenoise.grid(row=3, column=2)
btnFilterNoiseSP.grid(row=5, column=0)
btnFilterMedianDenoise.grid(row=5, column=1)
btnReset.grid(row=5, column=2)

root.mainloop()
