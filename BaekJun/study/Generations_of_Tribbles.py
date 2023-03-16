"""
https://www.acmicpc.net/problem/9507
"""

fibo = [1, 1, 2, 4]

for _ in range(4, 68):
    fibo.append(fibo[-1] + fibo[-2] + fibo[-3] + fibo[-4])
    
for _ in range(int(input())):
    print(fibo[int(input())])
    
