with open('finals.txt', 'r' , encoding='utf-8') as finals_file:
    finals_lines = finals_file.readlines()

with open('allseed.txt', 'r', encoding='utf-8') as allseed_file:
    allseed_lines = allseed_file.readlines()

newf = []
for line in finals_lines:
    line = line.strip()
    keep_line = True

    for allseed_line in allseed_lines:
        allseed_line = allseed_line.strip()

        if line == allseed_line:
            keep_line = False
            break

        if line[:4] == allseed_line[:4]:
            keep_line = False
            break

        if len(line) == 3 and len(allseed_line) >= 4 and line == allseed_line[:3]:
            keep_line = True
            break

        if len(allseed_line) < 3:
            continue

    if keep_line:
        newf.append(line)

with open('finals.txt', 'w') as finals_file:
    finals_file.write('\n'.join(newf))

print("Keep it cool!")
