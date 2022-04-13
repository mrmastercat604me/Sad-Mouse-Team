import time
import os
run = True
file_path = r'DATA.txt'
while run:
    with open(file_path, 'a+') as fp:
        inpt = input("[C]reate,[E]xit, [D]elete//ID, [U]pdate//ID, [R]ead //ID: ")
        #EXIT WORKINGS
        if inpt == "e" or inpt == "E":
            print("Goodbye")
            run = False
        #CREATE WORKINGS
        elif inpt == "c" or inpt == "C":
            name = input("Name?: ")
            id = input("Student_ID?: ")
            gpa = input("GPA?: ")
            fp.write(f"{id}\n")
            fp.write(f"{name}\n")
            fp.write(f"{gpa}\n")
            time.sleep(1)
            print("Added to Database")
            print("-"*10)
        #READ WORKINGS
        elif "r" in inpt or "R" in inpt:
            with open(file_path, 'r') as fpr:
                id_find = input("Student Id?: ")
                while fpr.tell() != os.fstat(fpr.fileno()).st_size:
                    id = fpr.readline().replace("\n", "")
                    name = fpr.readline().replace("\n", "")
                    gpa = fpr.readline().replace("\n", "")
                    if id == id_find:
                        print(id)
                        print(name)
                        print(gpa)

                        break
                else:
                    print("Student ID Not Found.")
                fpr.close
        #DELETE WORKINGS
        elif "d" in inpt or "D" in inpt:
            fileaslist = []
            id_find = input("id? ")
            with open( "DATA.txt", 'r') as fp:
                fileaslist = fp.readlines()
                fp.close()
            with open( "DATA.txt", 'w') as fp:
                for number , line in enumerate(fileaslist):
                    #PROBLEM IT WILL DELETE ANY LINE CONTAINING id_find
                    if id_find not in line:
                        fp.write(line)

        #UPDATE WORKINGS
        elif "u" in inpt or "U" in inpt:
            pass
    fp.close