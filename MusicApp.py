# Ameen Ahmed
# 7/13/17

from tkinter import *
from tkinter import ttk
import Web


class MusicApp:
    def __init__(self, master):
        self.master = master
        self.createGUI()

    def createGUI(self):

        # Configure master window
        bkgrnd = '#FF6161'
        self.master.configure(background=bkgrnd)
        self.master.title('MusicApp.py')
        self.master.resizable(False, False)

        # Style
        style = ttk.Style(self.master)
        style.configure('.', background=bkgrnd, font=('Arial Black', 12))

        # Frame creation
        self.entry_frame = ttk.Frame(self.master)
        self.entry_frame.pack()
        self.output_frame = ttk.Frame(self.master)

        # Entry_frame design
        ttk.Label(self.entry_frame, text='Song').grid(
            row=0, column=0, padx=100, sticky='w')
        ttk.Label(self.entry_frame, text='Artist').grid(
            row=0, column=2, padx=100, sticky='w')

        self.song = StringVar()
        self.artist = StringVar()

        ttk.Entry(self.entry_frame, textvariable=self.song).grid(row=1, column=0)
        ttk.Entry(self.entry_frame, textvariable=self.artist).grid(row=1, column=2)

        ttk.Button(self.entry_frame, text='Search',
                   command=lambda: self.callback(
                       self.song.get(), self.artist.get())).grid(row=2, column=1)


        # Output_frame design
        self.yt_link = StringVar()
        self.sc_link = StringVar()
        self.am_link = StringVar()

        self.yt_img = PhotoImage(file='icons/youtube-icon.png').subsample(3, 3)
        self.sc_img = PhotoImage(file='icons/soundcloud-icon.png').subsample(6, 6)
        self.am_img = PhotoImage(file='icons/audiomack-icon.png').subsample(2, 2)


        self.yt = ttk.Label(self.output_frame,
                            textvariable=self.yt_link,
                            compound=LEFT, image=self.yt_img).pack()
        self.sc = ttk.Label(self.output_frame,
                            textvariable=self.sc_link,
                            compound=LEFT, image=self.sc_img).pack()
        self.am = ttk.Label(self.output_frame,
                            textvariable=self.am_link,
                            compound=LEFT, image=self.am_img).pack()

    def callback(self, song, artist):
        self.yt_link.set(Web.youtube_search(song, artist))
        self.sc_link.set(Web.soundcloud_search(song, artist))
        self.am_link.set(Web.audiomack_search(song, artist))
        self.output_frame.pack()

def main():
    root = Tk()
    MusicApp(root)
    root.mainloop()

if __name__ == '__main__': main()