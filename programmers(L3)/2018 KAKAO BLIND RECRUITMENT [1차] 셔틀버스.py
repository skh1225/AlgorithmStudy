from collections import deque
from datetime import datetime, timedelta

def solution(n, t, m, timetable):
    answer = ''
    queue = deque(sorted(timetable))
    T = datetime.strptime('09:00', '%H:%M') - timedelta(minutes=t)
    prev = '00:00'
    for i in range(n):
        T += timedelta(minutes=t)
        cnt = 0
        for j in range(m):
            if queue:
                if T >= datetime.strptime(queue[0], '%H:%M'):
                    prev = queue.popleft()
                    cnt += 1
            else:
                return max(prev,f'{T.hour:02d}:{T.minute:02d}')
        if i == n-1:
            if cnt == m:
                prev = datetime.strptime(prev, '%H:%M')-timedelta(minutes=1)
                return f'{prev.hour:02d}:{prev.minute:02d}'
            else:
                return max(prev,f'{T.hour:02d}:{T.minute:02d}')