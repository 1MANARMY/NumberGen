import random

num_list = []
def random_number():
    # returns 10 numbers between 0 and 9
    for i in xrange(10):
        yield random.randint(0,9)

for n in random_number():
    var = num_list.insert(0, n)
print ''.join(str(n) for n in num_list)
