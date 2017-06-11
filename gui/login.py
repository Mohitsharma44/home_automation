from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Username: "))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text="pwd: "))
        self.pwd = TextInput(multiline=False, password=True)
        self.add_widget(self.pwd)

        self.add_widget(Label(text="2fac: "))
        self.tfa = TextInput(multiline=False)
        self.add_widget(self.tfa)


class SimpleKivy(App):
    def build(self):
        return LoginScreen()

if __name__ == "__main__":
    SimpleKivy().run()
