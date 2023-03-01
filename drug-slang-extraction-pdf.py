with open('cocaine.txt', 'r') as f:
    contents = f.read()

with open('cocaine.txt', 'w') as f:
    f.write(contents.replace(';', '\n'))