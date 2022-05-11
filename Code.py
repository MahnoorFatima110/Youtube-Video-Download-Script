from tkinter import *
from pytube import YouTube as YT
window = Tk()
window.geometry("800x800")
window.title("2k19 youtube download manager")
linkVariable=StringVar()
Label(window,text="Paste your link",font="arial 20 bold").pack()
Entry(window,width=50,textvariable=linkVariable).pack()
def downloads():
    url=YT(str(linkVariable.get()))
    format=url.streams.filter(progressive=True,file_extension="mp4")
    video=format.first()
    video.download()
Button(window,text="Click",font="arial 20 bold", bg="pink",command=downloads).pack()
window.mainloop()
