import time
from itertools import cycle

colors = [('red', 7), ('yellow', 2), ('green', 5), ('yellow', 2)]
color_dur = cycle(colors)

for t in range(4):
    a = next(color_dur)
    print(a[0])
    time.sleep(a[1])



colors = ['red', 'yellow', 'green', 'yellow']
duration = [7, 2, 5]
duration.append(duration[1])
color_dur = list(zip(colors, duration))

print(color_dur)
