def read_file(filename):
    try:
        with open(filename) as f:
            contents = f.readlines()
    except FileNotFoundError:
        pass
    else:
        print(contents)
        print(len(contents))


filename = ('cat.txt')
read_file(filename)