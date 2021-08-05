def reverseInGroups(arr, N, K):
    for i in range(0, N, K):
        st = i 
        end = min(i+K-1, N-1)
        while st < end:
            # print(st, end)
            arr[st], arr[end] = arr[end], arr[st]
            st += 1
            end -= 1

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    reverseInGroups(arr, 6, 6)
    print(arr)
