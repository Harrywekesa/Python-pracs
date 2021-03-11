ten_things = "Oranges ugali unga mchele waru six "
print("Wait these are not ten names lets fix this")
stuff = ten_things.split(' ')
more_stuff = ["Kenya", "Song", "Movie", "Matoke", "KPLC", "Girl", "Boy", "Hit"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} things now")

print("There we go:", stuff)
print("Lets do more things with lists")
print(stuff[0])
print([stuff[-1]])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
