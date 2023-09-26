import openai

def ChatGPT(Gesprochenes):
    text = Gesprochenes + ". Beantworte diese Frage in 3 Sätzen und auf Englisch"

    #openai.api_key = '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'
    #-- Neuer OPEN AI API Key einfügen --# 
    response = openai.Completion.create(
        engine='text-davinci-003', 
        prompt=text,
        max_tokens=50,  
        temperature=1.0,  
        n=1
    )

    if response.choices:
        return response.choices[0].text.strip()
    return None

def ChatGPT_temp():
    Antwort = "das ist meine antwort"
    return Antwort