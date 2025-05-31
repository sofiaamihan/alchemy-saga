from scripts.constants import *
from tkinter import *

def insert_text(text, widget):
    """Displays Text onto Message Log"""
    if widget is not None:
        widget.config(state=NORMAL)
        widget.insert(END, text)
        widget.config(state=DISABLED)
        widget.see(END)