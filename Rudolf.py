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

    def close():
        fenster.destroy()
        exit
    global fenster
    fenster = tk.Tk()
    fenster.title("Rudolf")
    w, h = fenster.winfo_screenwidth(), fenster.winfo_screenheight()
    fenster.overrideredirect(1)
    fenster.geometry("%dx%d+0+0" % (w, h))
    

    global label
    label = tk.Label(fenster, text="Drücke M zum aufnehmen deiner Frage", font=("Arial", 24), anchor="center" )
    #label.pack(padx=20, pady=20)
    label.place(relx=0.5, rely=0.5, anchor="center")


    button1 = tk.Button(fenster, text="Rudolf Beenden", command=close, width=20, height=3)
    button1.place(relx=0.5, rely=0.92, anchor="center")


    fenster.mainloop()



if __name__ == "__main__":
    # Einen Thread für die GUI erstellen
    gui_thread = threading.Thread(target=GUI)
    gui_thread.start()

    # Einen Thread für die Methode legLos erstellen
    leglos_thread = threading.Thread(target=Hirn)
    leglos_thread.start()
