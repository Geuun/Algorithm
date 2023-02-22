from itertools import permutations

"""
문제 설명
머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다.
조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다.
문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.
"""
"""
유의사항
네 가지를 붙여 만들 수 있는 발음 이외에는 어떤 발음도 할 수 없는 것으로 규정합니다.
예를 들어 "woowo"는 "woo"는 발음할 수 있지만 "wo"를 발음할 수 없기 때문에 할 수 없는 발음입니다.
"""

def solution(babbling):
    answer = 0
    
    canSpeek = ["aya", "ye", "woo", "ma"]
    
    words = []
    
    for _ in range(len(canSpeek)):
        for _ in permutations(canSpeek, _+1):
            words.append("".join(_))
            
    for _ in babbling:
        if _ in words:
            answer += 1
    
    return answer