def findMinDiff(arr,n,m):
        # code here
        arr.sort()
        if n < m:
            return -1
        
        minDiff = arr[n-1] - arr[0]
        for i in range(n-m+1):
            minDiff = min(minDiff, (arr[i+m-1] - arr[i]))