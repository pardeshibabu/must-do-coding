def count_pair(x, Y, n, frequency):
    import bisect
    if x==0:
        return 0
    if x == 1:
        return frequency[0]

    ans = 0
    ind = bisect.bisect_right(Y,x)
    ans += n-ind
    ans += (frequency[0] + frequency[1])

    if x == 2:
        ans -= frequency[3]
        ans -= frequency[4]
        return ans
    
    if x==3:
        ans += frequency[2]
    
    return ans




def countPairs(a,b,m,n):
    frequency = [0]*5
    for i in b:
        if i < 5:
            frequency[i] += 1

    a = sorted(a)
    b = sorted(b)

    c = 0
    for j in a:
        c += count_pair(j, b, n, frequency)
    
    return c


if __name__=='__main__':
    a = [2, 1, 6, 3]
    b = [1, 5 ,2]
    print(countPairs(a,b,3,2))

