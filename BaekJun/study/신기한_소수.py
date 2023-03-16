"""
https://www.acmicpc.net/problem/2023
"""
import sys

input = sys.stdin.readline

N = int(input())


# 소수인지 판별 (에라토스테네스의 체)
def is_prime(num: int) -> bool:
    for i in range(2, int(num**0.5) + 1):
        if int(num) % i == 0:
            return False
    return True


# DFS 탐색 (재귀)
def dfs(number: int):
    # N자리 수가 되면 출력
    if len(str(number)) == N:
        print(number)
    else:
        # 한자리씩 늘려가며 소수인지 판별
        for i in range(10):
            temp = number * 10 + i

            # 소수일 때 재귀
            if is_prime(temp) == True:
                dfs(temp)


# 한자리 숫자 중에 소수로 시작
dfs(2)
dfs(3)
dfs(5)
dfs(7)
