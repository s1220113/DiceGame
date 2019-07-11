import sys
import random

print('What is your name?')
name = raw_input()
print('Hello,' + name + '!')

print('Rolling the dice...')


total = 0
for i in range(2):
    print("Dice %d: " % (i+1)),
    result = random.randint(1, 6)
    total += result
    print(result)

print("Total value: %d" % total)
if total > 7:
    print('You won!')
else:
    print('You lost!')


