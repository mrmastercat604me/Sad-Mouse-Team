fileaslist = []
id_find = input("id? ")
with open( "DATA.txt", 'r') as fp:
    fileaslist = fp.readlines()
    fp.close()
with open( "DATA.txt", 'w') as fp:
    for number , line in enumerate(fileaslist):
        if id_find not in line:
            fp.write(line)
           