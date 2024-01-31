def delete_special(file_path):
    
    
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        new_lines = [line for line in lines if not any(letter in line for letter in "çşüöıwxâêôîûğ.,;!?-:)(–")]

       
        with open(file_path, "w", encoding="utf-8") as file:
            file.writelines(new_lines)

        print("Deleted.")


file_path = "finals.txt"  
delete_special(file_path)
