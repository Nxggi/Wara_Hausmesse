from Speech2Text import S2T
from Spracheingabe import Eingabe
from ChatGPT import ChatGPT
from ChatGPT import ChatGPT_temp
from Sprachausgabe import Sprachausgabe
import threading
import tkinter as tk
import keyboard




def Hirn():
    WAV_Pfad =""
    GPT_Antwort =""
    keyboard.wait("m")
    fenster.after(0, lambda: label.config(text="Recording..."))
    WAV_Pfad = Eingabe()
    fenster.after(0, lambda: label.config(text="Verarbeiten"))
    Gesprochenes = S2T(WAV_Pfad)
    print(Gesprochenes)
    #GPT_Antwort = ChatGPT(Gesprochenes) 
    GPT_Antwort = ChatGPT_temp()
    Sprachausgabe(GPT_Antwort)
    fenster.after(0, lambda: label.config(text=GPT_Antwort))
    fenster.after(0, lambda: label.config(text="Drücke M zum aufnehmen deiner Frage"))
    Hirn()



def GUI():
    global fenster
    fenster = tk.Tk()
    fenster.title("Rudolf")

    global label
    label = tk.Label(fenster, text="Drücke M zum aufnehmen deiner Frage", font=("Arial", 24))
    label.pack(padx=20, pady=20)

    fenster.mainloop()


if __name__ == "__main__":

    gui_thread = threading.Thread(target=GUI)
    gui_thread.start()

    leglos_thread = threading.Thread(target=Hirn)
    leglos_thread.start()
