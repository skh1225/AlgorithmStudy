def solution(commands):
    answer = []
    table = [[[''] for _ in range(51)] for _ in range(51)]
    for command in commands:
        result = method(command, table)
        if result:
            answer.append(result)
    return answer

def method(command, table):
    com = command.split()
    if com[0] == 'UPDATE':
        if len(com) == 4:
            r,c,value = com[1:]
            table[int(r)][int(c)][0] = value
        else:
            value1, value2 = com[1:]
            for i in range(51):
                for j in range(51):
                    if table[i][j][0] == value1:
                        table[i][j][0] = value2
    elif com[0] == 'MERGE':
        r1, c1, r2, c2 = map(int, com[1:])
        if table[r1][c1][0] != '':
            for i in range(51):
                for j in range(51):
                    if (i,j) != (r2,c2) and id(table[i][j]) == id(table[r2][c2]):
                        table[i][j] = table[r1][c1]
            table[r2][c2] = table[r1][c1]
        else:
            for i in range(51):
                for j in range(51):
                    if (i,j) != (r1,c1) and id(table[i][j]) == id(table[r1][c1]):
                        table[i][j] = table[r2][c2]
            table[r1][c1] = table[r2][c2]
    elif com[0] == 'UNMERGE':
        r, c = map(int, com[1:])
        for i in range(51):
            for j in range(51):
                if (i,j) != (r,c) and id(table[i][j]) == id(table[r][c]):
                    table[i][j] = ['']       
    else:
        r, c = map(int, com[1:])
        if table[r][c][0] != '':
            return table[r][c][0]
        else:
            return 'EMPTY'