from tkinter import *
from PIL import Image, ImageTk

photo1 = PhotoImage(file="./assets/home_screen_background.png")
mod_photo1 = photo1.subsample(2, 2)
mod_photo2 = ImageTk.PhotoImage(Image.open("./assets/isla.png").resize((150, 150)))
mod2_photo2 = ImageTk.PhotoImage(Image.open("./assets/isla.png").resize((200, 200)))
mod_photo3 = ImageTk.PhotoImage(Image.open("./assets/rosa.png").resize((150, 150)))
mod2_photo3 = ImageTk.PhotoImage(Image.open("./assets/rosa.png").resize((150, 150)))
mod_photo4 = ImageTk.PhotoImage(Image.open("./assets/jess.png").resize((150, 150)))
mod2_photo4 = ImageTk.PhotoImage(Image.open("./assets/jess.png").resize((150, 150)))
mod_photo5 = ImageTk.PhotoImage(Image.open("./assets/violet.png").resize((150, 150)))
mod2_photo5 = ImageTk.PhotoImage(Image.open("./assets/violet.png").resize((150, 150)))
mod_photo6 = ImageTk.PhotoImage(Image.open("./assets/merida.png").resize((150, 150)))
mod2_photo6 = ImageTk.PhotoImage(Image.open("./assets/merida.png").resize((150, 150)))
mod_photo7 = ImageTk.PhotoImage(Image.open("./assets/diego.png").resize((150, 150)))
mod2_photo7 = ImageTk.PhotoImage(Image.open("./assets/diego.png").resize((150, 150)))
photo8 = PhotoImage(file="./assets/versus.png")
mod_photo8 = photo8.subsample(10, 10)
