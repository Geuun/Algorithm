from itertools import permutations

def solution(ability):
    answer = 0
    
    # 종목 수
    event_num = len(ability[0])
    
    # 가능한 모든 경우의 수
    pm = list(permutations(ability, event_num))
    print(f'pm : {pm}')
    
    # 가능한 모든 경우의 수 중 가장 높은 점수 구하기
    for i in range(len(pm)):
        cnt = 0
        for j in range(len(pm[i])):
            cnt += pm[i][j][j]
            # print(f'i : {i}, j : {j}')
            # print(f'cnt : {cnt}')
        
        answer = max(answer, cnt)
        
    return answer

# solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]])
# solution([[20, 30], [30, 20], [20, 30]])