filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    print(lines)

print('\n')

for line in lines:
    line = line.lower().rstrip()
    print(line.replace('python', 'C'))



