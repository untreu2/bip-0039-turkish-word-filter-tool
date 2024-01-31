def remove_short_words_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = [line for line in lines if not shortest_word_length(line) < 4]

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

def shortest_word_length(line):
    words = line.split()
    shortest = min(len(word) for word in words)
    return shortest if words else 0

file_path = "finals.txt"

remove_short_words_lines(file_path)

print("Deleted.")
