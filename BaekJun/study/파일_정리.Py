"""
https://www.acmicpc.net/problem/20291
"""

import sys

input = sys.stdin.readline


def file_clean(N):
    file_dict = {}

    for _ in range(N):
        file_ext = input().rstrip().split(".")
        # print(file_ext)

        if file_ext[1] in file_dict:
            file_dict[file_ext[1]] += 1
        else:
            file_dict[file_ext[1]] = 1

    for _ in sorted(file_dict.items(), key=lambda x: x[0]):
        print(_[0], _[1])


N = int(input())
file_clean(N)
