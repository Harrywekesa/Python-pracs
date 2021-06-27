try:
    data = open("data zangu.txt", "rw")
    data.write("This is my test file for exception handling")
except IOError:
    print("Error: can't find file or read data")
else:
    print("Written content in the file was successful")
    data.close()