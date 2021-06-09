def MergeSort(A):
    '''mergesort of A and return new collection'''
    if len(A) < 2:
        return A
    mid = len(A)//2
    left = MergeSort(A[:mid])
    right = MergeSort(A[mid:])

    i = j = 0
    B = []
    while len(A) > len(B):
        if j >= len(right) or (i< len(left) and left[i] < right[j]):
            B.append(left[i])
            i +=1
        elif j < len(right):
            B.append(right[j])
            j +=1
    return B
import random
x = [random.randint(1,100) for x in range(10)]
print(x)
print(MergeSort(x))


