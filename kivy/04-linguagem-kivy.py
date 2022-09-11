from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Incrementador(BoxLayout):
    pass

class Test4(App):
    def build(self):
        return Incrementador()

Test4().run()