def trappingWater(arr, n):
    low = 0
    high = n-1
    leftMax = 0
    rightMax = 0
    result = 0
    while low <= high:
        if arr[low] < arr[high]:
            if arr[low] > leftMax:
                leftMax = arr[low]
            else:
                result += leftMax - arr[low]
            low += 1

        else:
            if arr[high] > rightMax:
                rightMax = arr[high]
            else:
                result += rightMax - arr[high]
            
            high -= 1
    return result


if __name__ == '__main__':
    arr = [6,9,9]
    print(trappingWater(arr, 3))
    