__author__ = 'm'
##############################################
# Программа выводит в случайно порядке слова #
# Слова на экране не повторяются             #
##############################################

import random

words = [
    "one",
    "two",
    "three",
    "four",
    "one",
    "four"
]

displayed_words = []

while words:
    position = random.randrange(len(words))
    if not words[position] in displayed_words:
        print(words[position], end=" ")
        displayed_words.append(words[position])
    words.remove(words[position])
