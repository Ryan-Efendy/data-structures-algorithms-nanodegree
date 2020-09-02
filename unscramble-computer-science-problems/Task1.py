"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('unscramble-computer-science-problems/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('unscramble-computer-science-problems/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

s = set()
for text in texts:
    s.add(text[0])
    s.add(text[1])

for call in calls:
    s.add(call[0])
    s.add(call[1])
    
print(f"There are {len(s)} different telephone numbers in the records.")