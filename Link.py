from tkinter import *
from tkinter import ttk


class Link:
    def __init__(self, **kwargs):
        self.provider = kwargs['provider']
        self.image = kwargs.get('image')
        self.link = StringVar()
        self.label = kwargs.get('label')
        self.status = BooleanVar()
        self.priority = kwargs.get('priority')