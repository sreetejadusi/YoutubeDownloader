import tkinter
from tkinter import *
from tkinter import filedialog
import pytube
filetypes = [("Audio", ".mp3")]
def downvideo():
    vidlink = pytube.YouTube(str(text.get()))
    video = vidlink.streams.get_highest_resolution()
    savepath = filedialog.askdirectory()
    video.download(savepath)
    Label(mainwin,
          text="Downloaded Video: {}".format(video.title),
          fg="red"
          ).pack(side=BOTTOM)

def downaudio():
    audlink = pytube.YouTube(str(text.get()))
    audio = audlink.streams.get_audio_only()
    savepath = filedialog.askdirectory()
    audio.download(savepath)
    Label(mainwin,
          text="Downloaded Audio: {}".format(audio.title),
          fg="red"
          ).pack(side=BOTTOM)

mainwin = Tk()
image = PhotoImage(file= 'ytd.png')
mainwin.title("Youtube Downloader")
mainwin.geometry("700x300")
mainwin.config(bg="white")
mainwin.iconphoto(True, image)

head = Label(mainwin,
             text="Youtube Downloader",
             fg="Black",
             bg="white",
             font=("Comic Sans", 20, "bold"),
             image=image,
             compound="bottom",

             ).pack()
me = Label(mainwin,
             text="Sree Teja Dusi",
             fg="Black",
             bg="white",
             font=("Lucida Handwriting", 5, "bold")
           ).pack(side=BOTTOM)

frameinput = Frame(mainwin)
framebutton = Frame(mainwin)
linktext = Label(frameinput,
                 text="Enter Youtube URL: ",
                 fg="red",
                 bg="white",
                 font=(20)
                 ).pack(side=LEFT)
text = StringVar()
linkinput = Entry(frameinput,
                  width=100,
                  textvariable = text,
                  fg="black",
                  bg="white",
                  ).pack(side=RIGHT)
buttonvideo = Button(framebutton,
                     text="Download Video",
                     command = downvideo,
                     fg="blue",
                     bg="white",
                     borderwidth=1,
                     background="white",
                     font=15,
                     padx=10,
                     ).pack(side=LEFT)
buttonaudio = Button(framebutton,
                     text="Download Audio",
                     command= downaudio,
                     fg="red",
                     bg="white",
                     borderwidth=1,
                     background="white",
                     font=15,
                     padx=10
                     ).pack(side=RIGHT)
buttonexit = Button(mainwin,
                    text="Exit",
                    command= exit,
                    fg="black",
                    bg="red",
                    borderwidth=1,
                    background="white",
                    font=10,
                    padx=10
                    ).pack(side=BOTTOM)

frameinput.pack()
framebutton.pack()
mainwin.mainloop()
