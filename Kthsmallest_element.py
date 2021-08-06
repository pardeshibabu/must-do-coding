def heapify(arr, n, i):
    large = i
    left = 2*i +1
    right = 2*i + 2

    if left < n and arr[left] > arr[i]:
        large = left
    
    if right < n and arr[right] > arr[large]:
        large = right
    
    if large != i:
        arr[i], arr[large] = arr[large], arr[i]
        heapify(arr, n, large)


def build_heap(arr, n):
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)

def heapSort(arr, n, k):
    build_heap(arr, n+1)
    for i in range(n, -1, -1):
        if i == k-1: return arr[0]
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


if __name__ == '__main__':
    # Using heapsort
    arr = [7, 10, 4, 20, 15]
    print(heapSort(arr, 4, 4))
    # print(arr)