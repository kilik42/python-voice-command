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
    if 'find location' in voice_data:
        location = record_audio('what is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        print('here is the location of '+ location)

print('say something')
voice_data = record_audio()
#print(voice_data)
respond(voice_data)
