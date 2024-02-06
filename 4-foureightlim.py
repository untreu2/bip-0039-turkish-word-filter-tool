def remove_short_words_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = [line for line in lines if not any(len(word) < 4 or len(word) > 8 for word in line.split())]

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

file_path = "finals.txt"

remove_short_words_lines(file_path)

print("Deleted.")
