nums = [value for value in range(1, 21)]

print(nums)

numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

numbers = list(range(1, 21))
print(numbers)


threes = []
for value in range(3, 30, 3):
    threes.append(value)

print(threes)


cubed = []
for value in range(1, 11):
    total = value ** 3
    cubed.append(total)

print(cubed)

cubed_simple = [value ** 3 for value in range(1, 11)]
print(cubed_simple)




