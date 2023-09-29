from Speech2Text import S2T
from Spracheingabe import Eingabe
from ChatGPT import ChatGPT
from ChatGPT import ChatGPT_temp
from Sprachausgabe import Sprachausgabe
from PIL import Image, ImageTk
import threading
import tkinter as tk
import keyboard
import time

running = True

def start_gif_thread():
    if __name__ == "__main__":
        gif_thread = threading.Thread(target=gif_vid)
        gif_thread.start()





def update_gif():
    try:
        gif_image.seek(gif_image.tell() + 1)
        frame = ImageTk.PhotoImage(gif_image)
        gif_label.configure(image=frame)
        gif_label.image = frame
        fenster.after(100, update_gif)
    except EOFError:
        # Das GIF ist am Ende, starte es von vorne
        gif_image.seek(0)
        update_gif()


def gif_vid():
    global gif_image
    global gif_label
    gif_image = Image.open(r"C:\Users\1000len-6476\Desktop\Wara Hausmesse\Loading.gif")


    frame = ImageTk.PhotoImage(gif_image)
    gif_label = tk.Label(fenster, image=frame)
    gif_label.pack()
    fenster.after(100, update_gif)
    fenster.mainloop()



def Error_bei_Speech2text():
    global running
    Error = "Das habe ich leider nicht verstanden, bitte stelle deine Frage erneut"
    fenster.after(0, lambda: label.config(text=Error))
    Sprachausgabe(Error)
    fenster.after(0, lambda: label.config(text="Drücke M zum Aufnehmen deiner Frage"))
    if running:
        Hirn()

def GUI():
    global fenster
    global label

    

def Hirn():
    global running
    hide_gif()
    while running:
        WAV_Pfad =""
        GPT_Antwort =""
        keyboard.wait("m")
        fenster.after(0, lambda: label.config(text="Recording..."))
        WAV_Pfad = Eingabe()
        show_gif()
        fenster.after(0, lambda: label.config(text="Verarbeiten"))
        Gesprochenes = S2T(WAV_Pfad)
        hide_gif()
        if Gesprochenes == "Error§$§$§$§$§$§$$$§":
            Error_bei_Speech2text()
    #    print(Gesprochenes)
    #    GPT_Antwort = ChatGPT(Gesprochenes) 
        GPT_Antwort = ChatGPT_temp()
        fenster.after(0, lambda: label.config(text=GPT_Antwort))
        Sprachausgabe(GPT_Antwort)
        time.sleep(1)
        fenster.after(0, lambda: label.config(text="Drücke M zum aufnehmen deiner Frage"))
        Hirn()




def hide_gif():
    gif_label.pack_forget()


def show_gif():
    gif_label.pack()

def update_gif():
    
    try:
        gif_image.seek(gif_image.tell() + 1)
        frame = ImageTk.PhotoImage(gif_image)
        gif_label.configure(image=frame)
        gif_label.image = frame
        fenster.after(100, update_gif)
    except EOFError:
        # Das GIF ist am Ende, starte es von vorne
        gif_image.seek(0)
        update_gif()

def GUI():
    global fenster
    global gif_label
    global gif_image
    def close():
        global running
        running = False
        fenster.destroy()
        exit()
    
    fenster = tk.Tk()
    fenster.title("Rudolf")
    fenster.configure(bg="white")
    w, h = fenster.winfo_screenwidth(), fenster.winfo_screenheight()
    fenster.overrideredirect(1)
    fenster.geometry("%dx%d+0+0" % (w, h))

    label = tk.Label(fenster, text="Drücke M zum Aufnehmen deiner Frage", font=("Arial", 24), anchor="center", bg="white")
    label.place(relx=0.5, rely=0.5, anchor="center")
   

    button1 = tk.Button(fenster, text="Rudolf Beenden", command=close, width=20, height=3)
    button1.place(relx=0.5, rely=0.92, anchor="center")

    
    fenster.mainloop()


def Hirn():
    global gif_label  
    global running
  
    while running:
        WAV_Pfad = ""
        GPT_Antwort = ""
        keyboard.wait("m")
        fenster.after(0, lambda: label.config(text="Recording..."))
        WAV_Pfad = Eingabe()
        start_gif_thread()
        Gesprochenes = S2T(WAV_Pfad)
        gif_label.pack_forget()
        if Gesprochenes == "Error§$§$§$§$§$§$$$§":
            Error_bei_Speech2text()
        GPT_Antwort = ChatGPT_temp()
        fenster.after(0, lambda: label.config(text=GPT_Antwort))
        Sprachausgabe(GPT_Antwort)
        time.sleep(1)
        fenster.after(0, lambda: label.config(text="Drücke M zum Aufnehmen deiner Frage"))




if __name__ == "__main__":
    gui_thread = threading.Thread(target=GUI)
    gui_thread.start()

    leglos_thread = threading.Thread(target=Hirn)
    leglos_thread.start()


    gif_thread = threading.Thread(target=gif_update)
    gif_thread.start()
