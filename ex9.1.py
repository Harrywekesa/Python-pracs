print("Enter the name of the file you want to change:")
file_name = input()
fname = open(file_name, 'w')

print("Truncating the file...")
fname.truncate()

print("Type int the required changes below three times:")
line1 = input("Line 1:")
line2 = input("Line 2:")
line3 = input("Line 3:")

print("Making the changes...")
fname.write(line1)
fname.write("\n")
fname.write(line2)
fname.write("\n")
fname.write(line3)

print("Done")

fname.close()
