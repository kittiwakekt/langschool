from kivy.app import App
from kivy.core import text
from kivy.uix.boxlayout import BoxLayout


class MainWidjet(BoxLayout):
    pass


class MainApp(App):
    def build(self):
        return MainWidjet()

MainApp().run()