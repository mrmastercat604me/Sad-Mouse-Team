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
            file_as_list = []
            with open( "DATA.txt", 'r') as fp:
                file_as_list = fp.readlines()
                fp.close()
            with open( "DATA.txt", 'w') as fp:
                id = input("ID: ")
                line = 0
                while line != (len(file_as_list)):
                    if id not in file_as_list[line]:
                        fp.write(file_as_list[line])
                        line += 1
                    elif id in file_as_list[line]:
                        line += 3
                fp.close

        #UPDATE WORKINGS
        elif "u" in inpt or "U" in inpt:
            pass
    fp.close