#Python program to create a 24-hour time format (HH:MM) using the 4 given digits. Display the latest time and do not use any digit more than once.

from itertools import permutations
from  datetime  import time

digits = [1, 2, 3, 4]
time_permutations = permutations(digits)

time="00:00"
valid_times = [f"{hour:02d}:{minute:02d}" for hour, minute in time_permutations if 0 <= hour * 10 + time[1] < 24 and 0 <= time[2] * 10 + time[3] < 60]
latest_time = max(valid_times, default="No valid time")

print(f"The latest valid time is: {latest_time}")
