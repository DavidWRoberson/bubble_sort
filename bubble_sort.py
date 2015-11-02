import random


numbers = []
x = 1
while(x < 1001):
	y = (random.random()) * 10000
	numbers.append(y)
	x += 1


def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist

print bubbleSort(numbers)


