def stockBuySell(A, n):
    profit = []
    i = 1
    while i < n:
        if A[i] > A[i-1]:
            cur_result = []
            cur_result.append(i-1)
            i += 1
            while i < n:    
                if A[i] > A[i-1]:
                    i += 1
                else:
                    break
            
            cur_result.append(i-1)
            profit.append(cur_result)
        
        i += 1
    
    return profit


if __name__ == '__main__':
    arr = [18, 11,  42,  49, 96, 23, 20, 49, 26, 26, 18, 73, 2, 53, 59, 34, 99, 25, 2]
    print(stockBuySell(arr, 5))
            
    