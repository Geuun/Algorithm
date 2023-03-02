def solution(input_string):
    answer = ""

    alpha_list = [input_string[0]]
    for i in input_string:
        if i != alpha_list[-1]:
            alpha_list.append(i)

    answer_dict = sorted(set(alpha_list))

    for i in answer_dict:
        cnt = 0
        for j in alpha_list:
            if i == j:
                cnt += 1
        if cnt > 1:
            answer += i

    if answer == "":
        answer += "N"

    return answer


# print(solution("edeaaabbccd"))
# print(solution("eeddee"))
# print(solution("string"))
# print(solution("zbzbz"))
# print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
