X = int(input())
d = [0]*(X+1)
while d[-1] == 0:
    for i in range(1,X+1):
        if i*5 <= X :
            if d[i*5] == 0:
                d[i*5] = d[i]+1
            elif d[i*5] > d[i]+1:
                d[i*5] = d[i]+1
        if i*3 <= X :        
            if d[i*3] == 0:
                d[i*3] = d[i]+1
            elif d[i*3] > d[i]+1:
                d[i*3] = d[i]+1
        if i*2 <= X :
            if d[i*2] == 0:
                d[i*2] = d[i]+1
            elif d[i*2] > d[i]+1:
                d[i*2] = d[i]+1
        if i+1 <= X :
            if d[i+1] == 0:
                d[i+1] = d[i]+1
            elif d[i+1] > d[i]+1:
                d[i+1] = d[i]+1
print(d[-1])
    

