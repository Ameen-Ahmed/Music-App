# Ameen Ahmed
# 7/13/17

from tkinter import *
from tkinter import ttk
import webbrowser
import Web
import Link


class MusicApp:
    def __init__(self, master):
        self.master = master
        self.createGUI()

    def createGUI(self):
        # Configure master window
        bkgrnd = '#AE2D58'
        self.master.configure(background=bkgrnd)
        self.master.title('MusicApp.py')
        self.master.resizable(False, False)

        # Style
        style = ttk.Style(self.master)
        style.configure('.', background=bkgrnd, font=('Arial Black', 8))
        style.configure('Link.TLabel', font=('Arial', 8, 'bold'), foreground='#0B00AB')
        style.configure('1.TCheckbutton', font=('Arial', 8))

        # Frame creation
        self.entry_frame = ttk.Frame(self.master)
        self.entry_frame.pack()
        self.output_frame = ttk.Frame(self.master)

        self.song = StringVar()
        self.artist = StringVar()

        # Entry Fields
        ttk.Label(self.entry_frame, text='Song').grid(
            row=0, column=0, padx=75, sticky='w')
        ttk.Label(self.entry_frame, text='Artist').grid(
            row=0, column=2, padx=75, sticky='w')
        ttk.Label(self.entry_frame).grid(
            row=0, column=1, padx=50, sticky='w')
        ttk.Entry(self.entry_frame, width=20,
                  textvariable=self.song).grid(row=1, column=0)
        ttk.Entry(self.entry_frame, width=20,
                  textvariable=self.artist).grid(row=1, column=2)

        # Check buttons
        self.my_dict={
            'Youtube': BooleanVar(),
            'SoundCloud': BooleanVar(),
            'Audiomack': BooleanVar()}

        ttk.Checkbutton(self.entry_frame, text='Youtube',
                        variable=self.my_dict['Youtube'], onvalue=True, offvalue=False,
                        style='1.TCheckbutton').grid(row=2, column=0, pady=10)

        ttk.Checkbutton(self.entry_frame, text='SoundCloud',
                        variable=self.my_dict['SoundCloud'], onvalue=True, offvalue=False,
                        style='1.TCheckbutton').grid(row=2, column=1, pady=10)

        ttk.Checkbutton(self.entry_frame, text='Audiomack',
                        variable=self.my_dict['Audiomack'], onvalue=True, offvalue=False,
                        style='1.TCheckbutton').grid(row=2, column=2, pady=10)

        ttk.Button(self.master, text='Search',
                   command=lambda: self.callback(
                       self.song.get(), self.artist.get(), self.my_dict)).pack(pady=10)

        # Output_frame design
        self.yt_link = StringVar()
        self.sc_link = StringVar()
        self.am_link = StringVar()


        #Images
        self.yt_img = PhotoImage(file='icons/youtube-icon.png').subsample(6, 6)
        ttk.Label(self.output_frame, image=self.yt_img).grid(row=0, column=0, pady=10)
        self.sc_img = PhotoImage(file='icons/soundcloud-icon.png').subsample(14, 14)
        ttk.Label(self.output_frame, image=self.sc_img).grid(row=1, column=0, pady=10)
        self.am_img = PhotoImage(file='icons/audiomack-icon.png').subsample(3, 3)
        ttk.Label(self.output_frame, image=self.am_img).grid(row=2, column=0, pady=10)


        #Output/ Links
        self.yt = ttk.Label(self.output_frame, cursor='hand2',
                            wraplength=350, textvariable=self.yt_link,
                            style='Link.TLabel', compound=LEFT)
        self.yt.grid(row=0, column=1, sticky='w', pady=10)
        self.yt.bind('<Button-1>', lambda e: self.link_callback(e, self.yt_link))

        self.sc = ttk.Label(self.output_frame, cursor='hand2',
                            wraplength=350, textvariable=self.sc_link,
                            style='Link.TLabel', compound=LEFT)
        self.sc.grid(row=1, column=1, sticky='w', pady=10)
        self.sc.bind('<Button-1>', lambda e: self.link_callback(e, self.sc_link))

        self.am = ttk.Label(self.output_frame, cursor='hand2',
                            wraplength=350, textvariable=self.am_link,
                            style='Link.TLabel', compound=LEFT)
        self.am.grid(row=2, column=1, sticky='w', pady=10)
        self.am.bind('<Button-1>', lambda e: self.link_callback(e, self.am_link))

    def callback(self, song, artist, providers):
        other_dict = {
            'Youtube': self.yt_link,
            'SoundCloud': self.sc_link,
            'Audiomack': self.am_link}

        for key, value in providers.items():
            if value.get():
                other_dict[key].set(Web.search(Link.Link(song, artist, key)))
                if other_dict[key] is None:
                    other_dict[key].set('SONG WAS NOT FOUND')
        self.output_frame.pack()

    def link_callback(self, event, link):
        webbrowser.open_new(link.get())

def main():
    root = Tk()
    MusicApp(root)
    root.mainloop()

if __name__ == '__main__': main()