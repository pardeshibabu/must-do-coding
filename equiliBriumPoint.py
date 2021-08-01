def equilibriumPoint(A, N):
    if N <= 0:
        return -1

    rightSum = sum(A)
    leftSum = 0
    pos = -1
    for i in range(N):
        rightSum -= A[i]
        if(leftSum==rightSum):
            pos = i + 1
            break
        leftSum += A[i]
    
    return pos

if __name__=='__main__':
    a = [1,3,5,2,2]
    print(equilibriumPoint(a, 5))
