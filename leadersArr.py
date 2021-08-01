def leaders(A, N):
    maxEle = A[N-1]
    stack = []

    for i in range(N-1, -1, -1):
        if maxEle <= A[i]:
            stack.append(A[i])
            maxEle = A[i]

    stack.reverse()
    return stack

if __name__=='__main__':
    a = [16, 17, 4, 3, 5, 2]
    print(leaders(a, 6))