#header
width = 40

School_name = 'Sainik Public School'
Consol_name = 'Teacher Console'

Teacher_login = {}
Student_login = {}
Student_info = {}

info_101 = print('Logged in succesfully')

error_101 = print('invalid username and password. Please try again')

def header():
    print('-' * width)
    print(School_name.center(width))
    print('-' * width)

def con():
    print('-' * width)
    print(Consol_name.center(width))
    print('-' * width)

def get_roll_number():
    return len(Student_info) + 1



def t_login():
    con()
    print('1)Get Result\n2)Search Roll number\n3)Enter student info\n4)Exit')
    ch = input('Enter your choice: ')
    if ch =='1':
        getresult()
    elif ch =='2' :
        srno()
    elif ch == '3':
        sinfo()
    elif ch == '4':
        exit(0)
    else:
        error_101

def srno():
    global Student_info
    search_name = input('Enter Name to search: ')
    
    found = False
    
    for rno, student in Student_info.items():
        if search_name.lower() in student['name'].lower():
            print(f'{student['name']}\t\t\t {rno}')
            found = True
    
    if not found:
        print('No students found with that name.')
    

def s_login():
    print('1)Get Result\n2)Search Roll number\n3Exit')
    ch = input('Enter your choice')
    if ch =='1' :
        getresult()
    elif ch =='2' :
        srno()
    elif ch =='3' :
        exit(0)
    else:
        error_101

def getresult():
    rno = int(input('Enter roll number: '))
    if rno in Student_info:
        header()
        print(f'Name         :  {Student_info[rno]['name']}')
        print(f'Roll Number  :  {rno}')
        print('-' * width)
        print(f'English      :   {Student_info[rno]['eng']}')
        print(f'Maths        :   {Student_info[rno]['mat']}')
        print('-' * width)
        per = ((Student_info[rno]['eng']+Student_info[rno]['mat'])*100)/200
        print(f'Percentage   :   {per}')
        if per >= 90:
                print('Rank   :   1')
        elif per >=75 and per < 90:
                print('Rank   :   2')
        elif per >=60 and  per < 75:
                print('Rank   :   3')
        elif per < 60 :
                print('Rank    :   4')
    else:
        print('Roll number not found.')
    
    
    

def sinfo():
    global Student_info
    rno = get_roll_number()
    name = input('Enter student name: ')
    eng = int(input('Enter English marks: '))
    mat = int(input('Enter Maths marks: '))
    Student_info[rno] = {'name' : name, 'eng' : eng, 'mat' : mat}

def main():
    while True:
        header()
        print('1)Teacher Login\n2)Student Login\n3)Exit')
        ch = input('Enter your choice: ')
        if ch == '1':
            user = input('Enter your username :')
            paswd = input('Enter your password :')
            tno = 1
            Teacher_login[tno] = {'user' : 'Pawan', 'paswd' : 'pawrik'}
            if user in Teacher_login[tno]['user'] and paswd in Teacher_login[tno]['paswd']:
                t_login()
            else:
                print('invalid username and password. Please try again')
        elif ch == '2':
            s_login()
        elif ch == '3':
            break
main()