def findElement(arr, n):
    leftMax = [None]*n
    rightMin = [None]*n

    leftMax[0] = arr[0]
    rightMin[n-1] = arr[n-1]

    for i in range(1, n):
        leftMax[i] = max(arr[i], leftMax[i-1])

    for i in range(n-2, -1, -1):
        rightMin[i] = min(arr[i], rightMin[i+1])

    for i in range(1, n-1):
        if leftMax[i-1] <= arr[i] and arr[i] <= rightMin[i+1]:
            return arr[i]

    return -1

if __name__ == '__main__':
    arr = [4, 2, 5, 7]
    print(findElement(arr, 4))
