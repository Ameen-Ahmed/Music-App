# Ameen Ahmed
# Started 7/13/17

from tkinter import *
from tkinter import ttk
import webbrowser
import Web
import Link
import Db
import os
import string

class MusicApp:
    def __init__(self, master):
        self.master = master
        self.createGUI()
        self.master.protocol("WM_DELETE_WINDOW", self.safe_close)

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

        # Song & Artist variables
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

        # Check buttons & Database creation
        self.youtube = Link.Link(provider='Youtube', priority=0)
        self.soundcloud = Link.Link(provider='SoundCloud', status=BooleanVar(), priority=2)
        self.audiomack = Link.Link(provider='Audiomack', status=BooleanVar(), priority=1)

        self.providers = {'Youtube': self.youtube,
                        'SoundCloud': self.soundcloud,
                        'Audiomack': self.audiomack}

        self.database = Db.Cache(self.providers)
        for key, value in self.providers.items():
            ttk.Checkbutton(self.entry_frame, text=key,
                        variable=value.status, onvalue=True, offvalue=False,
                        style='1.TCheckbutton').grid(row=2, column=value.priority, pady=10)

        # Search Button
        ttk.Button(self.master, text='Search',
                   command=lambda: self.callback(
                       string.capwords(self.song.get()), string.capwords(self.artist.get()), self.providers)).pack(pady=10)

        # Images
        self.youtube.image = PhotoImage(file=self.resource_path("icons\youtube-icon.png")).subsample(6, 6)
        self.soundcloud.image = PhotoImage(file=self.resource_path("icons\soundcloud-icon.png")).subsample(14, 14)
        self.audiomack.image = PhotoImage(file=self.resource_path("icons\\audiomack-icon.png")).subsample(3, 3)

    def callback(self, song, artist, providers):
        previous_search = self.database.check_data(song, artist)
        database_entry = [song, artist]

        for key, value in providers.items():
            if value.status.get():
                if previous_search:
                    self.database.update(song, artist, key)
                    web_link = self.database.retrieve(song, artist)[key]
                else:
                    web_link = Web.search_link(value, song, artist)
                    database_entry.append(web_link)

                ttk.Label(self.output_frame, image=value.image).grid(row=value.priority, column=0, pady=10)
                value.label = ttk.Label(self.output_frame, cursor='hand2', wraplength=350,
                                        textvariable=value.link, style='Link.TLabel')
                value.label.grid(row=value.priority, column=1, sticky='w', pady=10)
                value.link.set(web_link)

                if web_link != 'SONG NOT FOUND':
                    eval_link = lambda x: (lambda p: self.link_callback(x))
                    value.label.bind('<Button-1>', eval_link(value.link))
            else:
                database_entry.append("NO ENTRY")

        if not previous_search:
            self.database.insert(database_entry)

        self.database.disp_rows()
        self.output_frame.pack()

    def link_callback(self, link):
        webbrowser.open_new(link.get())

    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(relative_path)

    def safe_close(self):
        self.database.db.close()
        os.remove(self.database.filename)
        self.master.destroy()


def main():
    root = Tk()
    MusicApp(root)
    root.mainloop()

if __name__ == '__main__': main()