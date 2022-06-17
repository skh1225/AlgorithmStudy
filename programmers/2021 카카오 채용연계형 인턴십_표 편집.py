def solution(n, k, cmd):
    array = [['head', None, 0], [0, 'head', 1]]
    for i in range(1, n-1):
        array.append([i, i-1, i+1])
    array.extend([[n-1, n-2, 'tail'], ['tail', n-1, None]])
    removed = []
    result = ['O']*n
    k += 1
    for s in cmd:
        if s[0] == 'D':
            for _ in range(int(s.split()[-1])):
                k = array[k][2]+1
        elif s[0] == 'U':
            for _ in range(int(s.split()[-1])):
                k = array[k][1]+1
        elif s[0] == 'C':
            prev = array[k][1]
            next = array[k][2]
            removed.append(array[k])
            if next == 'tail':
                k = prev+1
                array[prev+1][2] = next
                array[n+1][1] = prev
            elif prev == 'head':
                k = next+1
                array[0][2] = next
                array[next+1][1] = prev
            else:
                k = next+1
                array[prev+1][2] = next
                array[next+1][1] = prev
        elif s[0] == 'Z':
            z = removed.pop()
            prev = z[1]
            next = z[2]
            if prev == 'head':
                array[0][2] = z[0]
                array[next+1][1] = z[0]
            elif next == 'tail':
                array[prev+1][2] = z[0]
                array[n+1][1] = z[0]
            else:
                array[prev+1][2] = z[0]
                array[next+1][1] = z[0]
    for r in removed:
        result[r[0]] = 'X'
    return ''.join(result)
