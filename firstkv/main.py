from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

Config.set('kivy', 'keyboard_mode', 'systemanddock')

# Window.size = (480, 853)


def get_ingridients(m):
    nitro = str(10 * m / 1000)
    salt = str(15 * m / 1000)
    starts = str(0.5 * m / 1000)
    dextstroze = str(5 * m / 1000)
    setting_time = str(round(m / 500 * 2))
    return dict(nitro=nitro, salt=salt, starts=starts, dextstroze=dextstroze,
                setting_time=setting_time)


class Container(GridLayout):
    def calculate(self):
        try:
            mass = int(self.text_input.text)
        except:
            mass = 0
        ingridients = get_ingridients(mass)
        self.salt.text = ingridients.get("salt")
        self.nitro.text = ingridients.get("nitro")
        self.sugar.text = ingridients.get("dextstroze")
        self.starts.text = ingridients.get("starts")
        self.time.text = ingridients.get("setting_time")


class FirstCatalogApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    app = FirstCatalogApp()
    app.run()
