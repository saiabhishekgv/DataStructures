
def binarySearch(a,key):
    if len(a)==0:
        return False
    else:
        midpoint = len(a)//2
        print a[midpoint]
        if a[midpoint] == key:
            return True
        elif a[midpoint]<key:
            return binarySearch(a[midpoint+1:],key)
        else:
            return binarySearch(a[:midpoint],key)
    return False

test = [3,5,6,8,11,12,14,15,17,18]
binarySearch(test,16)
binarySearch(test,8)

print 'thi'
for i in range(1,13):
    print '6//',i,6//i