'''
Authentication System with file handling
1:registration: name, email, pass, number (all validated)
2:login: email and pass (3 tries)
3:exit
'''
def registration():
    name = input("Enter name: ")
    phonestr = input("Enter phone no: ")
    if phonestr.isnumeric()==False:
        print("Registration process terminated. Enter only numeric value.")
        registration()
    phone=int(phonestr)
    if phone<=1000000000 or phone>10000000000:
        print("Registration process terminated. Please enter a valid phone no.")
        registration()
    email = input("Enter email: ")
    if not email.endswith('@gmail.com'):
        print("Registration process terminated. Please enter a valid email.")
        registration()
    passw = input('''Your password must have at least:
        One upper case 
        One lower case 
        One special case character 
        One integer value\n============================
    Enter password: ''')
    pass_upper = False
    pass_lower = False
    pass_num = False
    pass_special = False
    special_chars= ('[','@','_','!','$','%','^','&','*','(',')','<','>','?','/','|','}','{','~',':',']','#') #this took 5 mins
    
    
    for i in passw:
        if i.islower()==True:
            pass_lower = True
        if i.isupper()==True:
            pass_upper = True
        if i.isnumeric()==True:
            pass_num = True
        if i in special_chars:
            pass_special = True
    if  pass_upper == True and pass_lower == True and pass_num == True and pass_special == True:
        print("Password is strong.")
    else:
        print("Registration process terminated. Please enter a strong password.")
        registration()
    
    
    with open('data.txt','a') as d:
        d.write(f"\n{name} {phone} {email} {passw}")
        f.close()    
    print("=========================\nRegistration Successful.")
    

#registration() #this was done in 43 mins (including those 5 mins for special char list)

def login():
    email_input = input("Enter email: ")
    passw_input = input("Enter password: ")
    #global tries
    success=1
    
    with open('data.txt','r') as f:
        file_data = f.readlines()
        f.close()
        #print(file_data)
        
    for i in file_data:
        check_line = i
        data_split = check_line.split()
        if email_input == data_split[2] and passw_input == data_split[3]:
            print("Login Successful")
            print(f"Welcome {data_split[0]}")
            success = 0
            break
        
        if success==1:
            #tries = 0
            print("Incorrect email or password.")
            break
            #print(f"You have {tries} try/tries remaining.")
            #login()
            
        # if tries==0:
        #     print("You have no tries remaining. Please try again later.")
        #     break
        if success==0:
            break
    
print("Welcome to Authentication System\n======================")
while(True):
    print('''Select option:
    1.registration
    2.login
    3.exit
    ''')
    choice = int(input("Enter choice: "))
    if choice==1:
        registration()
    if choice==2:
        login()
    if choice==3:
        break

    

