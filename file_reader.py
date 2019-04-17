'''with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)'''





'''with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())'''


filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()


print(len(pi_string))

birthday = input('Enter your birthday, in the form of mmddyy: ')
if birthday in pi_string:
    print('Your birthday appears in the first million digits of pi!')
else:
    print('Your birthday doesnt appear in the first million digits of pi.')

