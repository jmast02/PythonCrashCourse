guest_list = ['Derek Jeter', 'Eminem', 'Mark Zuckerberg']

print('Would you like to go to dinner', guest_list[0],'?')
print('Would you like to go to dinner', guest_list[1],'?')
print('Would you like to go to dinner', guest_list[2],'?')

print(guest_list[2], 'cant make it.')

guest_list[2] = 'Steve Jobs'

print('Would you like to go to dinner', guest_list[0], '?')
print('Would you like to go to dinner', guest_list[1], '?')
print('Would you like to go to dinner', guest_list[2], '?')

guest_list.insert(0, 'Bryce Harper')
guest_list.insert(1, 'Trump')
guest_list.append('A-Rod')

print(guest_list)

sorry_alex = guest_list.pop()
sorry_steve = guest_list.pop()
sorry_eminem = guest_list.pop()
sorry_derek = guest_list.pop()

print(f"sorry {sorry_alex}, {sorry_steve}, {sorry_eminem}, {sorry_derek}, the able wont be here")

del guest_list[:]

print(guest_list)