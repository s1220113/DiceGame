import sys
import random

print('What is your name?')
name = raw_input()
print('Hello,' + name + '!')

print('Rolling the dice...')

while 1:
    total = 0
    for i in range(2):
        print("Dice %d: " % (i+1)),
        result = random.randint(1, 6)
        total += result
        print(result)

    print("Total value: %d" % total)
    if total > 7:
        print(name + ' won!')
    else:
        print(name + ' lost!')

    print('One more time? yes/no')
    flg = raw_input()
    if flg == 'yes':
        continue
    else:
        print('Good bye!')
        break
