file_name = input("Enter the file name: ")

try:
    with open(file_name, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)

    print("Number of lines in the file:", line_count)

except FileNotFoundError:
    print("The file was not found.")
except Exception as e:
    print("An error occurred:", e)

