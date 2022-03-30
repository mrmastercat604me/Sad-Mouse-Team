import time
run = True
file_path = r'saves.txt'
while run:
    with open(file_path, 'w+') as fp:
        inpt = input("[E]xit, Delete, Update, Read Student ID here:____, or [C]reate?: ")
        if inpt == "e" or inpt == "E":
            print("Goodbye")
            run = False
        elif inpt == "c" or inpt == "C":
            name = input("Name?: ")
            id = input("Student_ID?: ")
            gpa = input("GPA?: ")
            fp.write(f"{id} {name} {gpa}\n")
            time.sleep(2)
            print("Added to Database")
            print("-----------------------------")