
import itertools
l = list(itertools.permutations("1359"))
sum = 0
for i in l:
    n = int(''.join(i))
    print n
    sum += n

print 'sum : ' + str(sum)
