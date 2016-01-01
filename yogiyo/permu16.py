
import itertools
sum = 0
for r in range(1,16):
    for i in itertools.permutations("123456789abcdef", r):
        n = int(''.join(i), 16)
        print n
        sum += n

print 'sum : ' + str(sum)

