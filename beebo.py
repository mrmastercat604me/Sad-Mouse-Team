fileaslist = []
with open( "New Text Document.txt", 'r') as f:
    fileaslist = f.readlines()
    f.close()
with open( "New Text Document.txt", 'w') as fp:
    for number, line in enumerate(fileaslist):
        if number not in [1]:
            fp.write(line)
    fp.close
