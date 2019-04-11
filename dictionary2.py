programming_words = {
    'boolean': 'True or False',
    'float': 'decimal',
    'int': 'whole number',
    'dictionary': 'key, value pairs',
    'tuple': 'can not change',
    'loop': 'performs iterations',
    'python': 'best language!'
}

for k, v in programming_words.items():
    print(f"Key: {k}, Value: {v}")

print('\n')
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'thames': 'england'
}

for k, v in rivers.items():
    print(f"The {k.title()} runs through {v.title()}.")

print('\n')

for k in rivers.keys():
    print(f"our list has the following rivers: {k.title()}.")


