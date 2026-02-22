import pyttsx3
import PyPDF2
from PyPDF2 import PdfReader
from tkinter.filedialog import *
from tkinter.filedialog import askopenfilename
book= askopenfilename()
reader = PdfReader(book)
pages = len(reader.pages)


for i in range (pages):
    page = reader.pages[i]
    text = page.extract_text()
    player= pyttsx3.init()
    player.say(text)
    player.runAndWait()



