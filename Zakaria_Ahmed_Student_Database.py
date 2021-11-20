# Zakaria Ahmed
def add_student():
    database = input('enter the file path:')
    infile = open(database, "a") # opens the file in append mode
    id = str((input('enter your id:')))
    name = str(input('enter your name:'))
    semester = str(input('which semester are you in:'))
    year = str(input('which year are you in:'))
    number_of_courses = input('how many courses do you take:')
    data = f"\n{id}:{name}:{year}:{semester}:{number_of_courses}"
    infile.write(data) # appends the data above the file path given
    print('record added succesfully !')
    infile.close() # closes the file to prevent vulnerabilities
def edit_student():
    database = input('enter the file path:')
    infile = open(database, "r") # opens the file in read mode
    f = infile.readlines() # a variable with the lines in the given file
    new_list = []
    id = input('enter your id:')
    for line in f: # loops through each line in a variable named line
        for item in line.split(':'): # splits the line by ':' and loops through the list
            new_list.append(item) # appends  data into a new list so we can manipulate the data
        if id in new_list and len(id) == 4: # checks if Id is in the new list
            checker = input("[y]ear or [s]emester or [c]ourses)")
            if checker == "y":
                year = input('enter the year for school : ')
                infile = open("students.dat", "a")
                data_y = f"\n{year}"
                infile.write(data_y)
                infile.close()
                break
            elif checker == "s":
                semester = input('enter a value for semester : ')
                infile = open("students.dat", "a")
                data_s = f"\n{semester}"
                infile.write(data_s)
                infile.close()
                break
            elif checker == 'c':
                courses = input('enter how many courses your taking: ')
                data_c = f"\n{courses}"
                infile = open("students.dat", "a")
                infile.write(data_c)
                infile.close()
                break
        else:
            while True:
                print('Student id does not exist')
                break
    infile.close()
def remove_student():
    database = input('enter the file path:')
    infile = open(database, "r")
    f = infile.readlines()
    id = input('enter your id:')
    new_list = []
    for line in f:
        items = line.split(':')
        if items[0] != id:
            choice = input("Are you sure you want to remove the student data , input yes to continue :")
            if choice == 'yes':
                new_list.append(line)
                with open("students.dat", 'w') as write_file:
                    write_file.writelines(new_list) # appends the file without the specified id (removes line with id)
                break
            else: break
    infile.close()
def get_info():
    database = input('enter the file path:')
    infile = open(database, "r")
    f = infile.readlines()
    id = input('enter your id:')
    new_list = []
    for line in f:
        if line.split(':')[0] == id:
            line.strip('\n')
            new_list.extend(line.split(':'))
    print('Id:' + new_list[0])
    print('Name:' + new_list[1])
    print('Semester:' + new_list[2])
    print('Year:' + new_list[3])
    print('Number of Courses:' + new_list[4])
    infile.close()
def menu(): # a menu so the user can easily access the given options 
    print('Welcome to our students database')
    print('********************************************************'
        ' **  \n'
        ' **	Please choose one of the options below:\n'
        ' **	[a] to add new student record\n'
        ' **	[e] to edit an existing student record\n'
        ' **	[i] to get information about a student record\n'
        ' **	[r] to remove an existing student record \n'
        ' **	[q] to quit \n'
        ' ********************************************************\n')
    choice = input('pick:')
    while True:
        if choice == "a":
            add_student()
            break
        elif  choice == "e":
            edit_student()
            break
        elif choice == "r":
            remove_student()
            break
        elif  choice == "i":
            get_info()
            break
        elif  choice == "q":
            break
        else: print('Invalid choice, please enter a valid choice!')
menu() # Runs the entire code with all needed functions!
