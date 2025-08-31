import datetime 
#[1518-05-29 00:00] Guard #1151 begins shift

with open("./input_four.txt", "r") as f:
    lines = f.readlines()


    
lines_sorted = sorted(lines, key=lambda x: datetime.datetime.strptime(x[1:17], 
                                                                      '%Y-%m-%d %H:%M'))

string_new = ""
for