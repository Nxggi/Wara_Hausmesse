import openai

def ChatGPT(Gesprochenes):
    text = Gesprochenes +  "Schreibe deine Antwort so als würdest du in einer Konversation auf die Frage/ Aussage sinnvoll antworten "

    openai.api_key = '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'
    #-- Neuer OPEN AI API Key einfügen --# 
    response = openai.Completion.create(
        engine='text-davinci-003', 
        prompt=text,
        max_tokens=100,  
        temperature=1.0,  
        n=1
    )

    if response.choices:
        return response.choices[0].text.strip()
    return None

def ChatGPT_temp():
    Antwort = "das ist meine antwort"
    return Antwort
