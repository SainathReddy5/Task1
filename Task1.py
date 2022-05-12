from ast import pattern
import json
import re 

def register():

    with open("Data.json",'r') as file:
        data = file.read()
        data = json.loads(data)

    userids = list(data.keys())

    pattern='^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
    while True:
        email = input("Enter your E-mail: ")

        if email in userids:
            print("Email id already Exists,Try login")

        elif re.search(pattern, email):
            print("valid Email")
            break
        else:
            print("invalid Email")
        


    pattern = re.compile(r'')
    while True:
            password = input("Enter your Password: ")
            if 6 >= len(password) <= 16:
                print("Password too small or long ")
            elif re.search(r'[!@#$%^&*]',password)is None:
                print("Password must have Special character")
            elif re.search(r'\d',password) is None:
                print("Password must have Number")    
            elif re.search(r'[A-Z]',password) is None:
                print("Password must have Capital letter")
            elif re.search(r'[a-z]',password) is None:
                print("Password must have Small lettre")
            else:
                print("password valid, You are registered")
                break
    
    entry = { email : password }

    with open("Data.json",'r') as file:
        data = file.read()
        data = json.loads(data)

    data.update(entry)    

    j = json.dumps(data)

    with open('Data.json','w') as file:
        file.write(j)
        file.close()







def login():
    
    with open("Data.json",'r') as file:
        data = file.read()
        data = json.loads(data)

    userids = list(data.keys())

    Eemail=input("Enter Email address ")
    if Eemail not in userids:
        print("Email not found, Please Register ")
        print("Please Run the file again to register ")
        quit()
    
    for i in range(3):
        Epassword = input("Enter Password ")
        
        if data[Eemail] != Epassword:
            print("Password incorect, Try again ")
        else:
            print("you are logged in")
            quit()


    key = input("Forgot password ? (Y/N)")
    if key == 'Y':
        show_password(Eemail)
        
    elif key == 'N':
        print('Try again')


    
def show_password(email):
    with open("Data.json",'r') as file:
        data = file.read()
        data = json.loads(data)
    print(data[email])



#MAIN
command = input("Enter Login or Registration (L/R) ")

if command == 'L':
    login()
elif command == 'R':
    register()
else:
    print("Wrong Input")




            











