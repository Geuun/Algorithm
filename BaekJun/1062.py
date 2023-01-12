# 가르침 1062

import sys
from intertools import combinations

def input():
    return sys.stdin.readline()

N, K = map(int, input().split())

words = [input() for _ in range(N)]

# 배워야하는 글자
base_words = {'a', 'n', 't', 'i', 'c'}
learned_num = K - len(base_words)

# 배워야하는 글자가 K개보다 많으면 모든 단어를 읽을 수 있음 
# 배워야하는 글자가 K개보다 적으면 읽을 수 있는 단어가 없음
if learned_num < 0 :
    print(0)
    exit()
    
if K == 26 :
    print(N)
    exit()
    
wordList = []
for i in base_words:
    if len(set(list(i)) - base_words) == 0:
        continue
    else:
        wordList.append(set(list(i)) - base_words)
        
toLearn = set()
for wo in wordList:
    toLearn = toLearn | wo #합집합

if len(toLearn) <= learned_num: #무조건 다 배울 수 있음
    print(N)
    exit()

alphComb = combinations(toLearn,learned_num)

cntList = []
for comb in alphComb:
    cnt = 0
    for wordSet in wordList:
        if len(wordSet - set(comb)) == 0:
            cnt += 1
    cntList.append(cnt)

print(max(cntList))
