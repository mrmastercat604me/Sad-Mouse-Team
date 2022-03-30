import os
run = True
file_path = r'saves.txt'
while run:
    if os.path.exists(file_path):
        with open(file_path, 'w') as fp:
            inpt = input("[E]xit, Delete, Update, Read Student ID here:____, or [C]reate?: ").lower
            if inpt == "e":
                run = False
            if inpt == "c":
                name = input("Name?: ")
                id = input("Student_ID?: ")
                gpa = input("GPA?: ")
                fp.write(f"{id} {name} {gpa}\n")
    else:
        with open(file_path, 'x') as fp:
            pass