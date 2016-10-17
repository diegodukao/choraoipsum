from random import shuffle

WORDS = [
    "vagabundo",
    "skate",
    "charlie",
    "brown",
    "santos",
]


def generate(qt_words):
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

    return sentence

