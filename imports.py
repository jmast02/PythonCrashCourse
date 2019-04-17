#using different import functions

'''import sandwiches as s

s.make_sandwich('cheese', 'lettuce')'''

'''from sandwiches import make_sandwich

make_sandwich('tomato', 'peppers')'''

'''from sandwiches import make_sandwich as ms

ms('spinach', 'olives')'''

from sandwiches import *

make_sandwich('plain')
