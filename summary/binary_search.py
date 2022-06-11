def binaray_search(array, target, start, end):
    mid = (start+end)//2
    while start != mid:
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid
            mid = (start+end)//2
        else:
            start = mid
            mid = (start+end)//2
    return -1


array = list(range(1, 21, 2))
print(binaray_search(array, 9, 0, 9))
