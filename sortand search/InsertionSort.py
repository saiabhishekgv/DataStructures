def insertionSort(a):
    counter = 0
    for i in range(0,len(a)):
        index = a[i]
        j = i
        while (j > 0 and a[j - 1] > index):
            a[j] = a[j - 1]
            j -= 1
            counter += 1
        a[j] = index
    print a, counter

a = [1,2,3,4,5,6]
insertionSort(a)