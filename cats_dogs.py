def read_file(filename):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        msg = ('Sorry, cant find that file.')
        print(msg)
    else:
        print(len(contents))


filename = ('cats.txt')
read_file(filename)
