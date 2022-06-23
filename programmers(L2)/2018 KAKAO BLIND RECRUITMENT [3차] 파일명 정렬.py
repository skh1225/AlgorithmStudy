import re


def solution(files):
    answer = []
    answer = sorted(files, key=lambda x: (
        re.split(r'[0-9]+', x)[0].lower(), int(re.split(r'[a-z,A-Z, ,.,-]+', x)[1])))
    return answer
