print("Input the name of the file you want to open:", end=" ")
name = input()

txt = open(name)
print(txt.read())