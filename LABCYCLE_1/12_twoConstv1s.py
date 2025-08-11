file_name = input("Enter the file name: ")

try:
    with open(file_name, 'r') as file:
        lines = file.readlines()

    print("Lines containing '11':")
    for line in lines:
        if '11' in line:
            print(line.strip())

except FileNotFoundError:
    print("The file was not found.")
except Exception as e:
    print("An error occurred:", e)

