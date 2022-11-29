import tkinter as tk
import random

def piglatin(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    translation = ""
    for word in sentence:
        if vowels.__contains__(word[0]):
            word = word + 'ay' + ' '
            translation += word
        else:
            word = word[1:] + word[0] + 'ay' + ' '
            translation += word
    print(translation)
    get_words()


def get_words():
    witty_comments = ["Lemme make this easy for you, give me a sentence.",
                      "Don't underestimate me. Give me a sentence",
                      "gimme another",
                      "I translate english to a made up language called pig latin. Try me out",
                      "I'm so bored.",
                      "Are you still there?",
                      "don't leave me here alone O,O give me something to thinkk about",
                      "No matter what you say it'll be too easy. I'm like a computer or something",
                      "Gimme a entence",
                      "you know this works better than I suspected",
                      "Dude what time do you think it is",
                      "Go to sleep",
                      "This is no joke",
                      "Go eat some food every now and again. You're a disgrace",
                      "don't forget to set your alarm",
                      "my creator had way too much time on his hands",
                      "please adopt me",
                      "Alright. Peace out"]
    sentence = input(witty_comments[random.randrange(len(witty_comments))])
    words = sentence.split()
    return piglatin(words)
get_words()

root = tk.Tk()
