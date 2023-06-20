A = [i+1 for i in range(16)]
N = 16
T = [0 for _ in range(N+1)]

def update(I, V, T):
    prev = section_sum(I,I,T)
    while I < len(T):
        T[I] += V-prev
        I += (I & -I)

def prefix_sum(I, T):
    result = 0
    while I > 0:
        result += T[I]
        I -= (I & -I)
    return result

def section_sum(S,E,T):
    return prefix_sum(E, T)- prefix_sum(S-1, T)

for i in range(N):
    update(i+1,A[i],T)

print(T)
