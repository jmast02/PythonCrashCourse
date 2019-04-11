favorite_languages = {
    'JEn': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

poll_takers = ['jen', 'edward', 'bob', 'steve']


# created empty list to store the key in favorite languages
favorite_languages_key = []


# looped through names to present them as lower case.
for name in favorite_languages.keys():
    poll_taker_name = name.lower()
    favorite_languages_key.append(poll_taker_name)


# if JEn took the poll, we wouldn't tell jen to take the poll.
for name in poll_takers:
    print('\n',name.title())

    if name.lower() in favorite_languages_key:
        print('Thank you for already taking the poll,', name.title(), '.')
    else:
        print('Please take the poll', name.title(), '.')