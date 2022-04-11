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
        elif inpt == "r" or inpt == "R":
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
        elif inpt == "d" or inpt == "D":
            pass
        #UPDATE WORKINGS
        elif inpt == "u" or inpt == "U":
            pass
    fp.close
