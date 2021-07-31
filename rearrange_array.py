def rearrange_array(arr, n):
    min_ind = 0
    max_ind = n-1
    max_element = arr[n-1] + 1
    for i in range(n):
        if i%2==0:
            arr[i] = arr[i]+ ((arr[max_ind]%max_element)*max_element)
            max_ind -= 1
        else:
            arr[i] = arr[i]+ ((arr[min_ind]%max_element)*max_element)
            min_ind += 1
    
    for i in range(n):
        arr[i] = arr[i] // max_element