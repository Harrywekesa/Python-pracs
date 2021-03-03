from sys import argv

script, file_name = argv
print(f"We are going to erase the {file_name} file")
print("If you dont want this click ctrl-c")
print("If you want this click return\enter")
input("?")

print("Opening this file...")
target = open(file_name, 'w+')

print("Truncating this file...")
target.truncate()

print("Enter three lines")
line1 = input("Line 1:")
line2 = input("Line 2:")
line3 = input("Line 3:")

print("Writing the lines to file...")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

target.close()
