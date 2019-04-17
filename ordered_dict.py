from collections import OrderedDict

programming_words = {
    'boolean': 'True or False',
    'float': 'decimal',
    'int': 'whole number',
    'dictionary': 'key, value pairs',
    'tuple': 'can not change',
    'loop': 'performs iterations',
    'Python': 'best language!'
}

for k, v in programming_words.items():
    if k.lower() != 'python':
        print(f"{k}: {v}")
    else:
        #I just wanted to put python in all caps
        print(f"{k.upper()} : {v.upper()}")
