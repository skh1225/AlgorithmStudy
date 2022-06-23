from datetime import datetime


def solution(m, musicinfos):
    answer = '(None)'
    max_length = 0  # 가장 긴 재생 시간 저장
    infos = []  # [재생시간, 곡 제목, [코드]]
    for s in musicinfos:  # infos 구성
        tmp = s.split(',')
        t0 = datetime.strptime(tmp[0], '%H:%M')
        t1 = datetime.strptime(tmp[1], '%H:%M')
        tmp_m = []
        for i in range(len(tmp[3])):
            if tmp[3][i] == '#':
                tmp_m[-1] += '#'
            else:
                tmp_m.append(tmp[3][i])
        infos.append([(t1-t0).seconds//60, tmp[2], tmp_m])

    split_m = []  # 입력 m을 [코드] 로 저장
    for i in range(len(m)):  # split_m 구성
        if m[i] == '#':
            split_m[-1] += '#'
        else:
            split_m.append(m[i])

    for i in infos:  # infos 의 music과 split_m 비교
        for idx, c in enumerate(i[2]):
            # music의 재생시간 >= m의 첫 코드와 일치하는 music의 코드의 index + m의 재생시간
            if c == split_m[0] and len(split_m)+idx <= i[0]:
                for j in range(len(split_m)):
                    # 코드가 불일치하면 중단
                    if split_m[j] != i[2][(idx+j) % len(i[2])]:
                        break
                # 코드가 일치하면
                else:
                    # 이전 저장 코드보다 길면 answer 갱신
                    if i[0] > max_length:
                        max_length = i[0]
                        answer = i[1]
            else:
                continue
    return answer
