import sys

# ex
# 4 2 
# 1 1 1 1
# >3

# 10 5
# 1 2 3 4 2 5 3 1 1 2
# >3

def solution(N, M, arr):
    start, end = 0, 0
    total = arr[0]
    cnt = 0
    
    while True:
        if total < M:
            end += 1
            if end >= N:
                break
            total += arr[end]
        
        elif total == M :
            cnt += 1
            total -= arr[start]
            start += 1
        
        else:
            total -= arr[start]
            start += 1
            
    return cnt
            

N, M = map(int, input().split())
arr = list(map(int, input().split()))

print(solution(N, M, arr))