from random import randint
num_list = []
for trk in range(10):
    num_list.append(randint(1,10))

def min_fun(numlist):
    min = numlist[0]
    for value in numlist :
        if value <= min :
            min = value
    return min

def max_fun(numlist):
    max = numlist[0]
    for value in numlist :
        if value >= max :
            max = value
    return max

print('*' * 20)
print('num_list =',num_list)
print ("Min value = ", min_fun(num_list))
print ("Max value = ", max_fun(num_list))

