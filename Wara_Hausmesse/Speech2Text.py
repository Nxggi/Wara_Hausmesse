import speech_recognition as sr

def S2T(x):
    wav_file = x
    r = sr.Recognizer()

    with sr.AudioFile(wav_file) as source:

        audio = r.record(source)

        try:
            text = r.recognize_google(audio, language="de-DE")
            
        except sr.UnknownValueError:
            text =     "Error§$§$§$§$§$§$$$§"
    
    return text
