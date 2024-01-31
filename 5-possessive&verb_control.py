with open("finals.txt", "r", encoding="utf-8") as file:
    words = file.readlines()

cleaned_words = []
for word in words:
    word = word.strip() 
    if not word.endswith(("m", "n", "i", "miz", "niz", "leri", "ler", "lar","de","da","ken","suna","sine","sına","süne","ine","ına","ıyla","uyla","ayla","eyle","leriyle","larıyla")):
        cleaned_words.append(word)

with open("finals.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(cleaned_words))

print("Deleted.")

