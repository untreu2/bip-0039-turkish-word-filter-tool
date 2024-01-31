with open('finals.txt', 'r') as file:
    lines = file.readlines()

# Büyük harf içeren satırları filtrele
filtered_lines = [line for line in lines if not any(char.isupper() for char in line)]

# Dosyayı tekrar yaz
with open('finals.txt', 'w') as file:
    file.writelines(filtered_lines)

print("Deleted.")