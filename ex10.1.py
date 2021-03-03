from os.path import exists

print("Name the file you want to make a copy of:")
from_file = input()
print("Name the destination file:")
to_file = input()
print(f"Checking the existence of {to_file} file.Does it exist? {exists(to_file)}")
input("Click enter. If False a new file with the name {} will be created".format(to_file)) 
in_file = open(from_file)
in_data = in_file.read()

out_file = open(to_file, 'w')
out_file.write(in_data)

in_file.close()
out_file.close()


