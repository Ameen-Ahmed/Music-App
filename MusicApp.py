# Ameen Ahmed
# 7/13/17

from tkinter import *
from tkinter import ttk
import Web
import webbrowser
import lxml


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
        style.configure('.', background=bkgrnd, font=('Arial Black', 10))
        style.configure('Link.TLabel', font=('Arial', 10, 'bold'), fg='blue')

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

        self.yt_img = PhotoImage(file='icons/youtube-icon.png').subsample(5, 5)
        self.sc_img = PhotoImage(file='icons/soundcloud-icon.png').subsample(12, 12)
        self.am_img = PhotoImage(file='icons/audiomack-icon.png').subsample(3, 3)

        self.yt = ttk.Label(self.output_frame, cursor='hand2',
                            wraplength=500,
                            textvariable=self.yt_link, style='Link.TLabel',
                            compound=LEFT, image=self.yt_img)
        self.yt.pack(anchor='w', pady=20)
        self.yt.bind('<Button-1>', lambda e: self.link_callback(e, self.yt_link))

        self.sc = ttk.Label(self.output_frame, cursor='hand2',
                            wraplength=500,
                            textvariable=self.sc_link, style='Link.TLabel',
                            compound=LEFT, image=self.sc_img)
        self.sc.pack(anchor='w', pady=20)
        self.sc.bind('<Button-1>', lambda e: self.link_callback(e, self.sc_link))

        self.am = ttk.Label(self.output_frame, cursor='hand2',
                            wraplength=500,
                            textvariable=self.am_link, style='Link.TLabel',
                            compound=LEFT, image=self.am_img)
        self.am.pack(anchor='w', pady=20)
        self.am.bind('<Button-1>', lambda e: self.link_callback(e, self.am_link))

    def callback(self, song, artist):
        self.yt_link.set(Web.youtube_search(song, artist))
        self.sc_link.set(Web.soundcloud_search(song, artist))
        self.am_link.set(Web.audiomack_search(song, artist))
        self.output_frame.pack()

    def link_callback(self, event, link):
        webbrowser.open_new(link.get())

def main():
    root = Tk()
    MusicApp(root)
    root.mainloop()

if __name__ == '__main__': main()