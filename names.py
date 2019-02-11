from random import shuffle
names = []

while True:
    name = input("Add your name, if ended enter 1\n")
    if name == '1':
        break
    names.append(name)

print("Added {} names".format(len(names)))

shuffle(names)

for i in range(len(names)):
    print("{}:{}".format(names[i], names[(i + 1) % len(names)]))
