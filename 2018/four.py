import datetime 
import collections
#[1518-05-29 00:00] Guard #1151 begins shift

with open("./input_four.txt", "r") as f:
    lines = f.readlines()


    
lines_sorted = sorted(lines, key=lambda x: datetime.datetime.strptime(x[1:17], 
                                                                      '%Y-%m-%d %H:%M'))

string_new = ""
for i in lines_sorted:
    string_new += i

print(string_new)

def create_dic(input):
    guard_dic = {}
    for line in input:
        
        if "Guard" in line:
            current_guard = line[19:].split(" ")[1]
            if current_guard not in guard_dic:
                guard_dic[current_guard] = 0 
                
            continue
        
        if "asleep" in line:
            sleep_start = datetime.datetime.strptime(line[1:17], '%Y-%m-%d %H:%M')
            
        if "wakes" in line:
            sleep_end = datetime.datetime.strptime(line[1:17], '%Y-%m-%d %H:%M')
            duration = (sleep_end - sleep_start).seconds // 60
            guard_dic[current_guard] += duration
            
    return guard_dic
    

    

guard_list = create_dic(lines_sorted)
print(guard_list)


print(max(guard_list, key = guard_list.get))
print(guard_list['#499'])


from collections import defaultdict

import datetime
from collections import defaultdict

# Read file
with open("./input_four.txt", "r") as f:
    lines = f.readlines()

# Sort by timestamp
lines_sorted = sorted(lines, key=lambda x: datetime.datetime.strptime(x[1:17], '%Y-%m-%d %H:%M'))

def analyze_guards(logs):
    guard_dic = defaultdict(int)               # guard -> total minutes asleep
    minute_map = defaultdict(lambda: [0]*60)  # guard -> list of 60 minute counts
    
    current_guard = None
    sleep_start = None

    for line in logs:
        timestamp = datetime.datetime.strptime(line[1:17], '%Y-%m-%d %H:%M')
        
        if "Guard" in line:
            current_guard = line.split()[3]   # e.g. "#1151"
        
        elif "falls asleep" in line:
            sleep_start = timestamp
        
        elif "wakes up" in line:
            sleep_end = timestamp
            duration = (sleep_end - sleep_start).seconds // 60
            guard_dic[current_guard] += duration
            
            # update minute map
            for m in range(sleep_start.minute, sleep_end.minute):
                minute_map[current_guard][m] += 1
    
    return guard_dic, minute_map


# Run analysis
guard_dic, minute_map = analyze_guards(lines_sorted)

# Part 1: Guard with the most total minutes asleep
sleepiest_guard = max(guard_dic, key=guard_dic.get)
sleepiest_minute = minute_map[sleepiest_guard].index(max(minute_map[sleepiest_guard]))
print("Part 1 -> Guard:", sleepiest_guard, "Minute:", sleepiest_minute,
      "Answer:", int(sleepiest_guard[1:]) * sleepiest_minute)

# Part 2: Guard most frequently asleep on the same minute
max_minute_count = 0
best_guard = None
best_minute = None

for guard, minutes in minute_map.items():
    most_common_minute = max(minutes)
    if most_common_minute > max_minute_count:
        max_minute_count = most_common_minute
        best_guard = guard
        best_minute = minutes.index(most_common_minute)

print("Part 2 -> Guard:", best_guard, "Minute:", best_minute,
      "Answer:", int(best_guard[1:]) * best_minute)