article = input("Türkçe dilinde herhangi bir yazı girin...")

lower_article = article.lower()
words = lower_article.split()

for finals in words:
    print(finals)

with open("finals.txt", "w", encoding="utf-8") as file:
    for finals in words:
        file.write(finals + "\n")

print("Okay!")

