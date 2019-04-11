vacation_spots = ['Austin', 'NY', 'Italy', 'Colorado', 'Spain']

print(vacation_spots)
print(sorted(vacation_spots))
print(vacation_spots)
vacation_spots.reverse()
print(vacation_spots)
vacation_spots.reverse()
print(vacation_spots)
vacation_spots.sort()
print(vacation_spots)
vacation_spots.sort(reverse=True)
print(vacation_spots)
print('\n')
print(f"my vacation spots include {len(vacation_spots)} places.")

vacation_spots.sort()
print(vacation_spots)

print(f"my first 3 spots are: {vacation_spots[:3]}")
print(f"my middle 3 spots are: {vacation_spots[1:-1]}")
print(f"my last 3 spots are: {vacation_spots[-3:]}")