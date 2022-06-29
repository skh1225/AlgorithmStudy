def solution(n, build_frame):
    answer = []
    for command in build_frame:
        if command_det(n, answer[:], command):
            if command[3] == 0:
                answer.remove(command[:3])
            else:
                answer.append(command[:3])
    return sorted(answer)


def command_det(n, result, command):
    x, y = command[0], command[1]
    if x < 0 or x > n-command[2] or y < 0 or y > n-1+command[2]:
        return False
    if command[3] == 1:
        if element_det(result, command[:3]):
            return True
        return False
    else:
        removed = command[:3]
        if removed in result:
            result.remove(removed)
        else:
            return False
        for r in result:
            if element_det(result, r) == False:
                result.append(removed)
                return False
        return True


def element_det(result, element):
    x, y = element[0], element[1]
    if element[2] == 1:
        tmp = [False]*2
        for r in result:
            if r in [[x, y-1, 0], [x+1, y-1, 0]]:
                return True
            elif r == [x-1, y, 1]:
                tmp[0] = True
            elif r == [x+1, y, 1]:
                tmp[1] = True
            if tmp[0] and tmp[1]:
                return True
    else:
        if y == 0:
            return True
        for r in result:
            if r in [[x-1, y, 1], [x, y-1, 0], [x, y, 1]]:
                return True
    return False
