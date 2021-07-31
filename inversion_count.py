
def merge(Arr, temparr, left, right, mid):
    i = left
    j = mid+1
    k = left
    ic = 0
    while i <= mid and j <= right:
        if Arr[i] <= Arr[j]:
            temparr[k] = Arr[i]
            i += 1
        else:
            temparr[k] = Arr[j]
            j += 1
            ic += (mid - i + 1)
        k += 1
    # Checking if any element was left
    while i <= mid:
        temparr[k] = Arr[i]
        i += 1
        k += 1

    while j <= right:
        temparr[k] = Arr[j]
        j += 1
        k += 1
    
    for m in range(left, right+1):
        Arr[m] = temparr[m]
    
    return ic


def merge_sort(arr, temp_arr, left, right):
    ic = 0
    if left < right:
        mid = (left + right)//2

        ic += merge_sort(arr, temp_arr, left, mid)
        ic += merge_sort(arr, temp_arr, mid+1, right)

        ic += merge(arr, temp_arr, left, right, mid)
    return ic

def ms(arr):
    n = len(arr)
    tmpArr = [0]*n
    return merge_sort(arr, tmpArr, 0, n-1)


if __name__=='__main__':
    arr=[4, 3, 5, 1, 2]

    print(ms(arr))
    print(arr)