file_name = input("Enter the file name: ")
search_word = input("Enter the word to search: ")
replace_word = input("Enter the word to replace it with: ")

try:
    with open(file_name, 'r') as file:
        content = file.read()

    updated_content = content.replace(search_word, replace_word)

    with open(file_name, 'w') as file:
        file.write(updated_content)

    print("Word replaced successfully!")

except FileNotFoundError:
    print("The file was not found.")
except Exception as e:
    print("An error occurred:", e)

