# Zakaria Ahmed
#py -m pip install paramiko
import paramiko
def add_student():
    infile = open("students.dat", "a")
    id = str((input('enter your id:')))
    name = str(input('enter your name:'))
    semester = str(input('which semester are you in:'))
    year = str(input('which year are you in:'))
    number_of_courses = input('how many courses do you take:')
    data = f"\n{id}:{name}:{year}:{semester}:{number_of_courses}"
    infile.write(data)
    print('record added succesfully !')
    infile.close()
def edit_student(): # append
    infile = open("students.dat", "r")
    f = infile.readlines()
    new_list = []
    id = input('enter your id:')
    for line in f:
        for item in line.split(':'):
            new_list.append(item)


        if id in new_list and len(id) == 4:
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


def remove_student():
    infile = open('students.dat', 'r')
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
                    write_file.writelines(new_list)
                break
            else: break


def get_info():
    infile = open('students.dat','r')
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

def ssh():
    ssh = paramiko.SSHClient()#creates the ssh client
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # adds to known list to avoid yes/no confirmation
    hostname_input = str(input('enter hostname:'))
    username_input = str(input('enter username:'))
    password_input = str(input('enter passcode:'))
    port_number_input = str(input('enter port number :'))
    ssh.connect(hostname=hostname_input,username=username_input,password=password_input,port=port_number_input) # default port number is 22 for ssh # use ip address for hostname
    print("you have succesfully connected to the server")
    print("ssh connection option is best used when using simple commands such as making files/directroires !")

    while True:

        print('********************************************************'
              ' **  \n'
              ' **	Please choose one of the options below:\n'
              ' **	[y] to continue and add commands \n'
              ' **	[q] to quit \n'
              ' ********************************************************\n')
        user_choice = input('enter a choice:')

        if user_choice == 'y':

            cmd = input("enter the command you want to make:")
            stdin, stdout, sterr = ssh.exec_command(cmd)


        elif user_choice == 'q':
            print('your connection is closed')
            ssh.close()
            break
        else:
            print('Invalid choice, please enter a valid choice!')



def main():

    print('Welcome to our students database')
    print('********************************************************'
        ' **  \n'
        ' **	Please choose one of the options below:\n'
        ' **	[a] to add new student record\n'
        ' **	[e] to edit an existing student record\n'
        ' **	[i] to get information about a student record\n'
        ' **	[r] to remove an existing student record \n'
        ' **	[s] to ssh into a local server and add commands \n'  
        ' **	[f] to transfer student database file  \n'
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
        elif  choice == "s":
            ssh()
            break

        elif  choice == "f":
            file_transfer()
            break
        elif  choice == "d":
            download()
            break
        else: print('Invalid choice, please enter a valid choice!')


def file_transfer():
    ssh = paramiko.SSHClient()#creates the ssh client
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # adds to known list to avoid yes/no confirmation
    hostname_input = str(input('enter hostname:'))
    username_input = str(input('enter username:'))
    password_input = str(input('enter passcode:'))
    port_number_input = str(input('enter port number , (default port is 22):'))
    ssh.connect(hostname=hostname_input,username=username_input,password=password_input,port=port_number_input) # default port number is 22 for ssh # use ip address for hostname
    print("you have succesfully connected to the server")
    full_pwd_of_file = str(input('enter relative path of file you choose to transfer:'))
    destination_path= str(input('enter absolute path of where you want the file to be stored in :'))
    sftp_client = ssh.open_sftp()
    print('file is being uploaded ....')
    sftp_client.put(full_pwd_of_file,destination_path)
    sftp_client.close()
    ssh.close()
    print('file is uploaded')
    print('sftp connection is closed')

def download():
    ssh = paramiko.SSHClient()  # creates the ssh client
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # adds to known list to avoid yes/no confirmation
    hostname_input = str(input('enter hostname:'))
    username_input = str(input('enter username:'))
    password_input = str(input('enter passcode:'))
    port_number_input = str(input('enter port number , (default port is 22):'))
    ssh.connect(hostname=hostname_input, username=username_input, password=password_input, # connects to ssh server
                port=port_number_input)  # default port number is 22 for ssh # use ip address for hostname if dns server is down
    print("you have succesfully connected to the server")
    full_pwd_of_file = str(input('enter absolute path of file you choose to transfer:'))
    destination_path = str(input('enter relative path of where you want the file to be stored in :'))
    sftp_client = ssh.open_sftp()
    print('file is being downloaded ....')
    sftp_client.get(full_pwd_of_file, destination_path)
    sftp_client.close()
    ssh.close()
    print('file is uploaded')
    print('sftp connection is closed')
main()# calls all the code
