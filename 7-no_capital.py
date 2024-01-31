with open('finals.txt', 'r') as file:
    lines = file.readlines()

filtered_lines = [line for line in lines if not any(char.isupper() for char in line)]

with open('finals.txt', 'w') as file:
    file.writelines(filtered_lines)

print("Deleted.")
