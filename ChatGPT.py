import openai

def ChatGPT(Gesprochenes):
    text = Gesprochenes + ". Beantworte diese Frage in 3 Sätzen, Schreibe deine Antwort so als würdest du in einer Konversation auf die Frage antworten"

    openai.api_key = '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'
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

#def ChatGPT_temp():
#    Antwort = "das ist meine antwort"
#    return Antwort
