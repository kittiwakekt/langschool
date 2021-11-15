from kivy.app import App
from kivy.core import text
from kivy.uix.boxlayout import BoxLayout
# WARNING: The scripts buildozer and buildozer-remote are installed in '/home/kittiwake/.local/bin' which is not on PATH.
# Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

class MainWidjet(BoxLayout):
    pass


class MainApp(App):
    def build(self):
        return MainWidjet()

MainApp().run()