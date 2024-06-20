def is_sorted(arr):
    n=len(arr)
    for i in range(1,n):
        if(arr[1-i]<=arr[i]):
            continue
        else:
            return False
    return True
arr=[1,2,3,4,5]
print(is_sorted(arr))