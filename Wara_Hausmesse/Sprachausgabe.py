from gtts import gTTS
import pygame
import os
video_path = "C:\Video.mp4"

def Sprachausgabe(text, language='de'):
    tts = gTTS(text=text, lang=language, slow=False,)
                   
    Verzeichnis = os.path.dirname(os.path.realpath(__file__))
    
    output_path = os.path.join(Verzeichnis, "output.mp3")
    
    tts.save(output_path)
    pygame.mixer.init()
   
    sound = pygame.mixer.Sound(output_path)

    sound.play()

    pygame.time.wait(int(sound.get_length() * 1000))  # Wartezeit in Millisekunden

    os.remove(output_path)
   
