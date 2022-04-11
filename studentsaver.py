import time
run = True
file_path = r'saves.txt'
while run:
    with open(file_path, 'a+') as fp:
        inpt = input("[C]reate,[E]xit, [D]elete//ID, [U]pdate//ID, [R]ead //ID: ")
        if inpt == "e" or inpt == "E":
            print("Goodbye")
            run = False
        elif inpt == "c" or inpt == "C":
            name = input("Name?: ")
            id = input("Student_ID?: ")
            gpa = input("GPA?: ")
            fp.write(f"{id} {name} {gpa}\n")
            time.sleep(1)
            print("Added to Database")
            print("-"*10)
        elif inpt == "r" or inpt == "R":
            with open(file_path, 'r') as fpr:
                linecount = 0
                for linecount, line in enumerate(fpr):
                    pass
                print(f"Total Lines: {linecount}")
                id_find = input("Student Id?: ")
    fp.close