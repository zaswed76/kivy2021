from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class Container(BoxLayout):
    pass

class MainApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    app = MainApp()
    app.run()