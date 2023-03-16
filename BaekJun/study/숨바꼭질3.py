import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

list = [0] * 100001
list[N] = 1

queue = deque()
queue.append(N)

while queue:
    now = queue.popleft()

    if now == K:
        print(list[now] - 1)
        break

    for next in [now - 1, now + 1, now * 2]:
        if (0 <= next < 100001) & (list[next] == 0):
            if next == now * 2:
                list[next] = list[now]
                queue.appendleft(next)
            else:
                list[next] = list[now] + 1
                queue.append(next)
