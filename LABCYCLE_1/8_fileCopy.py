
source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")

try:
    with open(source_file, 'r') as src:
        content = src.read()
    with open(destination_file, 'w') as dest:
        dest.write(content)
    print("File copied successfully!")

except FileNotFoundError:
    print("The source file does not exist.")
except Exception as e:
    print("An error occurred:", e)

