def findSmallest(arr):
    small = arr[0]
    small_index = 0
    for i in range(1,len(arr)):
        if arr[i] < small:
            small = arr[i]
            small_index = i
    return small_index

def selectionSort(arr):
    ordered = []
    for _ in range(len(arr)):
        element = findSmallest(arr)
        ordered.append(arr[element])
        arr.pop(element)
    return ordered

if __name__ == "__main__":
    list = [12,4,7,0,8]
    print(selectionSort(list))


        

