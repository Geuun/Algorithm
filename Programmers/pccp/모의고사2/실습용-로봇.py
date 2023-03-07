def solution(command):
    """
    R: 오른쪽으로 90도 회전
    L: 왼쪽으로 90도 회전
    G: 앞으로 한 칸 이동
    B: 뒤로 한 칸 이동
    """
    x = 0
    y = 0

    # 나아갈 방향
    d = 0
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    for _ in command:
        if _ == "R":
            d = (d + 1) % 4  # 0, 1, 2, 3
        elif _ == "L":
            d = (d - 1) % 4  # 0, 3, 2, 1
        elif _ == "G":
            x = x + direction[d][0]
            y = y + direction[d][1]
        elif _ == "B":
            x = x - direction[d][0]
            y = y - direction[d][1]

    answer = [x, y]

    return answer
