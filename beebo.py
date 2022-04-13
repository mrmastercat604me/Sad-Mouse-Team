l1 = []
with open( "New Text Document.txt", 'r') as fp:
    l1 = fp.readlines()
with open( "New Text Document.txt", 'w') as fp:
    for number, line in enumerate(l1):
        if number not in [1]:
            fp.write(line)
