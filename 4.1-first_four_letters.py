filename = 'finals.txt'

with open(filename, 'r', encoding='utf-8') as file:
    lines = file.readlines()

filtered_lines = [line for line in lines if len(line) < 4 or len(set(line[:4])) > 1]

with open(filename, 'w', encoding='utf-8') as file:
    file.writelines(filtered_lines)