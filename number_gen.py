import random
num_list = []
def random_number():
    # returns 10 numbers between 1 and 10
    for i in xrange(10):
        yield random.randint(1,10)

for n in random_number():
    num_list.insert(0, n)
print num_list
