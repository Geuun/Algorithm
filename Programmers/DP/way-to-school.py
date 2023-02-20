# 프로그래머스 등굣길
# https://school.programmers.co.kr/learn/courses/30/lessons/42898?language=python3

def solution(m, n, puddles):
    
    # 2차원 배열(DP) 생성
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # print(dp)
    
    # 시작점 ( 문제에서 1, 1 로 지정 )
    dp[1][1] = 1
    
    # puddle 을 -1 로 표시
    for i, j in puddles:
        dp[j][i] = -1
        
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            
            # 시작점은 continue
            if i == 1 and j == 1:
                continue
            
            # puddle 이면 0
            if dp[i][j] == -1:
                dp[i][j] = 0
            else:
                dp[i][j] += dp[i - 1][j] + dp[i][j - 1]
                
    return dp[n][m] % 1000000007

if __name__ == "__main__":
    
    m, n = 4, 3
    puddles = [[2, 2]]
    
    answer = solution(m, n, puddles)
    
    print(answer)