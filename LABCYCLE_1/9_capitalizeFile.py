src = input("Enter source file name: ")
dest = input("Enter destination file name: ")

try:
    with open(src, 'r') as f1, open(dest, 'w') as f2:
        for line in f1:
            f2.write(line.upper())  # Convert entire line to uppercase

    print("File content capitalized and saved.")

except FileNotFoundError:
    print("Source file not found.")
except Exception as e:
    print("An error occurred:", e)
