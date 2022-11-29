def reverser(word):
    new_word = ''
    temp = word
    if word.isalpha():
        for x in range(len(word)):
            new_word += temp[(x+1)*-1]
        print(new_word)
        reverser(input('moar'))
    else:
        print("That ain't a word")
        reverser(input('Try again!'))


reverser(input("Gimme a word and I'll reverse it."))
