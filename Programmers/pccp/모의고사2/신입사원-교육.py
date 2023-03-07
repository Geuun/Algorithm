import heapq

def solution(ability, number):
    answer = []

    # heap 구조에 ability 넣기
    for _ in ability:
        heapq.heappush(answer, _)  # answer = [0, 1, 2, 3, 4]

    for _ in range(number):
        # 작은 두수 x, y 뽑아서 더하기
        x = heapq.heappop(answer)
        y = heapq.heappop(answer)

        advanced_num = x + y

        # 다시 넣기
        heapq.heappush(answer, advanced_num)
        heapq.heappush(answer, advanced_num)

    return sum(answer)
