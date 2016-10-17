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
        sentence = "Chorao Ipsum vagabundo brown"
        for i in range(int(qt_words)):
            if not words:
                words = WORDS.copy()
            shuffle(words)
            if i % 7 == 0:
                sentence = "{}{}".format(sentence, ",")
                sentence = "{} {}".format(sentence, words.pop())
            elif i % 11 == 0:
                sentence = "{}{}".format(sentence, ".")
                sentence = "{} {}".format(sentence, words.pop().capitalize())
            else:
                sentence = "{} {}".format(sentence, words.pop())

        self.root.body.ipsumarea.text = sentence

if __name__ == "__main__":
    ChoraoIpsum().run()
