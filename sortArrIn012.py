def sort012(arr,n):
    # code here
    zeros = arr.count(0)
    ones = arr.count(1)
    twos = arr.count(2)
    i = 0
    while zeros > 0:
        arr[i] = 0
        zeros -= 1
        i += 1
    
    while ones > 0:
        arr[i] = 1
        i += 1
        ones -= 1
    
    while twos > 0:
        arr[i] = 2
        i += 1
        twos -= 1



if __name__=='__main__':
    a = [0, 2, 1, 2, 0]
    sort012(a, 5)
    print(a)