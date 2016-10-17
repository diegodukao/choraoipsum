from kivy.app import App
from random import shuffle

WORDS = [
    "vagabundo",
    "skate",
    "charlie",
    "brown",
    "santos",
]


class ChoraoIpsum(App):

    def generate(self, qt_words):
        words = WORDS.copy()
        sentence = ""
        for i in range(int(qt_words)):
            if not words:
                words = WORDS.copy()
            shuffle(words)
            sentence = "{} {}".format(sentence, words.pop())

        print(sentence)

if __name__ == "__main__":
    ChoraoIpsum().run()
