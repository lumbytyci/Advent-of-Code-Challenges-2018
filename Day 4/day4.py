#Timestamps are written using year-month-day hour:minute format.
from datetime import datetime
import collections
data = [line.strip("\n") for line in open("input.txt").readlines()]

data.sort() # Works because they are using ISO 8601
        
guards = collections.defaultdict(list)
times = collections.defaultdict(int)

for line in data:
    time, event = line.split("] ")
    time = time[15:17]

    if event.startswith("Guard"):
        guard = int(event.split()[1][1:])
    elif event == "falls asleep":
        start = int(time)
    elif event == "wakes up":
        end = int(time)
        guards[guard].append((start, end))
        times[guard] += (end- start)

(guard, time) = max(times.items(), key=lambda i: i[1])
(minute, count) = max([(minute, sum(1 for start, end in guards[guard] if start <= minute < end)) for minute in range(60)], key=lambda i: i[1])

print('part 1:', guard * minute)

(guard, minute, count) = max([
    (guard, minute, sum(1 for start, end in guards[guard] if start <= minute < end))
for minute in range(60) for guard in guards], key=lambda i: i[2])

print('part 2:', guard * minute)

