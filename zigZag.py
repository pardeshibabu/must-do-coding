def zigZag(arr, n):
    for i in range(n-1):
        if i%2==0:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        else:
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    print(arr)
    
if __name__ == '__main__':
    arr = [4, 3, 7, 8, 6, 2, 1, 9]
    zigZag(arr, 8)