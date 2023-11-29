import pyaudio
import wave
import keyboard

def Eingabe():
    
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 2
    fs = 44100
    filename = f"C:\\Text_fuer_Rudolf.wav"  # Pfad für die WAV-Datei

    # Interface erstellen
    p = pyaudio.PyAudio()


    print("M gedrückt halten zum aufnehmen")
    keyboard.wait("m")
    frames = []  # Framestorage

    # Aufnahme startet
    y = 1
    stream = p.open(format=sample_format,
                            channels=channels,
                            rate=fs,
                            frames_per_buffer=chunk,
                            input=True)
    while True:

        data = stream.read(chunk)
        frames.append(data)
        if not keyboard.is_pressed("m") and y == 1:
            break

    # Aufnahme stoppen und Interface schließen
    stream.stop_stream()
    stream.close()

    print('Finished recording')

    # Als WAV speichern
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()


    
    return filename
