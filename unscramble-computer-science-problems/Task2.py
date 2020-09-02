"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('unscramble-computer-science-problems/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('unscramble-computer-science-problems/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

d = {}
for call in calls:
    d[call[0]] = d.get(call[0], 0) + int(call[3])
    d[call[1]] = d.get(call[1], 0) + int(call[3])
    
telp_num = list(d.keys())[0]
for key, val in d.items():
    if val > d[telp_num]:
        telp_num = key
        
print(f"{telp_num} spent the longest time, {d[telp_num]} seconds, on the phone during September 2016.")
