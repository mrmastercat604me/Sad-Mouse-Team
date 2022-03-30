import os
run = True
while run:
    file_path = r'saves.txt'
    inpt = input("[E]xit, Delete, Update, Read Student ID here:____, or [C]reate?: ").lower
    if inpt == "e":
        run = False
    if inpt == "c":
        if os.path.exists(file_path):
            with open(file_path, 'w') as fp:
                name = input("Name?: ")
                id = input("Student_ID?: ")
                gpa = input("GPA?: ")
                fp.write(f"{id} {name} {gpa}\n")
        else:
            with open(file_path, 'x') as fp:
                pass