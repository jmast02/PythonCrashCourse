def count_words(filename, word):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        msg = ('Sorry, cant find that file.')
        print(msg)
    else:

        words = contents.count(word)
        print(words)



filename = ('common_words.txt')
count_words(filename, 'the')
