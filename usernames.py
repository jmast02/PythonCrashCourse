usernames = ['jmast02', 'jonm02', 'jonmast02', 'jm02', 'admin']


if usernames:
    for user in usernames:
        if user == 'admin':
            print('welcome', user, 'would you like to see a report?')
        else:
            print('welcome', user, 'thanks for logging back in!')
else:
    print('we need user names!')

print('\n')
current_users = ['USER1', 'user2', 'user3', 'user4', 'user5']

new_users = ['user1', 'user2', 'user6', 'user7', 'user8']

current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())

for user in new_users:
    if user.lower() in current_users_lower:
        print(user, 'username already taken.')
    else:
        print('you may use', user)




