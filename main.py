from kivy.app import App
from choraogenerator import generate


class ChoraoIpsum(App):

    def generate(self, qt_words):
        sentence = generate(qt_words)
        self.root.main_panel.body.ipsumarea.text = sentence

if __name__ == "__main__":
    ChoraoIpsum().run()
