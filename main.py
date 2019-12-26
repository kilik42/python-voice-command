import speech_recognition as sr
from time import ctime

r = sr.Recognizer()


def record_audio():
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            print("sorry I did not get that")
        except sr.RequestError:
            print('Sorry, my speech service is down')
        return voice_data

def respond(voice_data):
    if 'what is your name' in voice_data:
        print('my name is alexis ')
    if 'what time is it' in voice_data:
        print(ctime())
    if 'search' in voice_data:
        search = record_audio('what do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('here is what i found for '+ search)

print('say something')
voice_data = record_audio()
#print(voice_data)
respond(voice_data)
