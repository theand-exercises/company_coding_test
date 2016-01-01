
import itertools
#l = list(itertools.permutations("12456789abcdefghjklmnoprstuvwxyz"))
sum = 0
for i in itertools.permutations("12456789abcdefghjklmnoprstuvwxyz"):
    n = int(''.join(i), 36)
    print n
    sum += n

print 'sum : ' + str(sum)

