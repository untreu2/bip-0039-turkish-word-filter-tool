with open('finals.txt', 'r') as finals:
    finals_lines = finals.readlines()

with open('allseed.txt', 'r') as allseed:
    allseed_lines = allseed.readlines()

match = set(line[:4] for line in finals_lines).intersection(line[:4] for line in allseed_lines)

filtered = []
for line in finals_lines:
    if line[:4] not in match and line not in allseed_lines:
        filtered.append(line)

with open('finals.txt', 'w') as finals:
    finals.writelines(filtered)
    
print("Process completed.")
