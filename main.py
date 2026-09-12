from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

import pyttsx3
import webbrowser

# Text To Speech
engine = pyttsx3.init()

def speak(text):
    print("ASSISTANT:", text)
    engine.say(text)
    engine.runAndWait()

class AssistantApp(App):

    def build(self):

        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        self.label = Label(text="My Voice Assistant")

        btn_google = Button(text="Open Google")
        btn_google.bind(on_press=self.open_google)

        btn_youtube = Button(text="Open YouTube")
        btn_youtube.bind(on_press=self.open_youtube)

        btn_facebook = Button(text="Open Facebook")
        btn_facebook.bind(on_press=self.open_facebook)

        btn_name = Button(text="What is your name?")
        btn_name.bind(on_press=self.tell_name)

        btn_love = Button(text="I Love You")
        btn_love.bind(on_press=self.love_reply)

        btn_exit = Button(text="Exit")
        btn_exit.bind(on_press=self.stop_app)

        layout.add_widget(self.label)
        layout.add_widget(btn_google)
        layout.add_widget(btn_youtube)
        layout.add_widget(btn_facebook)
        layout.add_widget(btn_name)
        layout.add_widget(btn_love)
        layout.add_widget(btn_exit)

        speak("Hello Irfan Sir. I am your personal assistant.")

        return layout

    def open_google(self, instance):
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    def open_youtube(self, instance):
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    def open_facebook(self, instance):
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    def tell_name(self, instance):
        speak("My name is Faini")

    def love_reply(self, instance):
        speak("Oh it seems lovely. I love you too")

    def stop_app(self, instance):
        speak("Goodbye")
        App.get_running_app().stop()

AssistantApp().run()