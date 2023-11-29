from gtts import gTTS
import pygame
import os


def Sprachausgabe(text, language='de'):
    # Erstellen Sie ein gTTS-Objekt
    tts = gTTS(text=text, lang=language)
    
    # Holen Sie sich das aktuelle Verzeichnis des Skripts
    current_directory = os.path.dirname(os.path.realpath(__file__))
    
    # Erstellen Sie den Dateipfad für die Ausgabedatei im aktuellen Verzeichnis
    output_path = os.path.join(current_directory, "output.mp3")
    
    # Speichern Sie die Sprachausgabe als Ausgabedatei
    tts.save(output_path)

    # Initialisieren Sie pygame Mixer
    pygame.mixer.init()

    # Laden Sie die Audiodatei als Sound-Objekt
    sound = pygame.mixer.Sound(output_path)

    # Spielen Sie die Audiodatei ab
    sound.play()

    # Warten, bis die Wiedergabe beendet ist
    pygame.time.wait(int(sound.get_length() * 1000))  # Wartezeit in Millisekunden

    # Löschen Sie die Ausgabedatei nach dem Abspielen
    os.remove(output_path)


    






