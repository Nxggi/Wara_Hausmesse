import pyttsx3


def Sprachausgabe(GPT_AW):
    #Die Antwort von GPT wird hier per Sprachausgabe und Textfeld ausgegeben
    s = pyttsx3.init()    
    s.setProperty('rate', 150)  

    voices = s.getProperty('voices')
    german_voice_id = (s, "de_DE", "Till")
    for voice in voices:
        if "german" in voice.languages:
            german_voice_id = voice.id
            break
    if german_voice_id:
        s.setProperty('voice', german_voice_id)
    s.say(GPT_AW)
    s.runAndWait()