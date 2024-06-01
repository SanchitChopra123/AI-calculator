from tkinter import Tk, Label, Frame, Entry, FLAT, Button, PhotoImage
import speech_recognition as sr
import pyttsx3
import operator
from PIL import ImageTk, Image, ImageOps

root = Tk()
root.title("Calculator")
root.maxsize(400,360)
root.geometry("400x360")

image=Image.open("bgx1.png")
# Resize the image using resize() method
resize_image = image.resize((750,420))
img = ImageTk.PhotoImage(resize_image)
# # Set background image

label6 = Label(image=img)
label6.image = img
label6.pack()

mic_img = Image.open("micx.png")
photo = ImageTk.PhotoImage(mic_img)
mic_img_label = Label(image=photo, bg='#040405')
mic_img_label.image = photo
mic_img_label.place(x=173, y=200)

#for mic access
r = sr.Recognizer()
my_mic_device = sr.Microphone(device_index=1)

# Adjust the threshold level
with my_mic_device as source:
    r.adjust_for_ambient_noise(source, duration=0.5)
    r.energy_threshold = 1000

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # for voice


def oper_type(op):
    return {
        '+': operator.add,
        '-': operator.sub,
        'x': operator.mul,
        '*': operator.mul,
        '/': operator.__truediv__,
        'Mod': operator.mod,
        'mod': operator.mod,
        '^' : operator.pow,
        'power': operator.pow,
    }[op]


def expr_fxn(op1, oper, op2):
    op1, op2 = int(op1), int(op2)
    return oper_type(oper)(op1, op2)


def calculate(event=None):
    with my_mic_device as source:
        print("Say What you want to calculate....")
        audio = r.listen(source)

    my_string = r.recognize_google(audio)
    print(my_string)

    result = expr_fxn(*(my_string.split()))
    print(result)

    engine.say("The result is " + str(result))
    engine.runAndWait()


mic_img_label.bind('<Button-1>', calculate)

root.mainloop()
