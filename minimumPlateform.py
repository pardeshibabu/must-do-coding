def minimumPlatform(n,arr,dep):
    arr.sort()
    dep.sort()
    max_plateform = 1
    currentBusyPlateform = 1

    i= 1
    j = 0
    while i < n and j < n:
        if(arr[i] <= dep[j]):
            i += 1
            currentBusyPlateform += 1
            if currentBusyPlateform > max_plateform:
                max_plateform = currentBusyPlateform
        else:
            j += 1    
            currentBusyPlateform -= 1

    return max_plateform
        

if __name__=='__main__':
    arr = [900, 1100, 1235]            
    dep = [1000, 1200, 1240]
    print(minimumPlatform(3, arr, dep))
