from Speech2Text import S2T
from Spracheingabe import Eingabe
from ChatGPT import ChatGPT
from ChatGPT import ChatGPT_temp
from Sprachausgabe import Sprachausgabe


WAV_Pfad = Eingabe()
Gesprochenes = S2T(WAV_Pfad)
print(Gesprochenes)
#GPT_Antwort = ChatGPT(Gesprochenes) 
GPT_Antwort = ChatGPT_temp()
Sprachausgabe(GPT_Antwort)
