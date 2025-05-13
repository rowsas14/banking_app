import os
from datetime import datetime

customer = {}

#admin checking
def check_admin():
 
    if not os.path.exists("admin_account.txt"):
        print("No admin account\n plese create one")
        create_admin()
    else:
        admin_login()    


#admin create
def create_admin():

    ad_username=input("--Ender admin user name : ")
    ad_password=input("--Ender admin password  : ")

    with open("admin_account.txt", "w") as file:
        file.write(f"{ad_username},{ad_password}")
    print("admin account created")    
    
 #admin Login
 
def admin_login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        with open("admin_account.txt", "r") as file:
            ad_username, ad_password = file.read().strip().split(",")
        if username == ad_username and password == ad_password:
            print("Login successful.\n")
            admin_menu()
        else:
            print("Invalid username or password.\n")
    except FileNotFoundError:
        print("Admin account file not found. Please create an account first.\n")
        create_admin()
 
#  #account number create      
 
def acc_number_create():
    try:
        with open("customer.txt", "r") as files:
            lines = files.readlines()
            if not lines:
                return "ACC001"
            last_line = lines[-1]
            last_acc_num = last_line.split()[0]  
            last_num = int(last_acc_num.replace("ACC", ""))
            return f"ACC{last_num + 1:03}"  
    except FileNotFoundError:
        return "ACC001"



#account create

def account_create():
    global customer
  
    name=input("enter name")
    while True:
         age=input("enter age")  
         if not age.isdigit():
             print("age is a number")
         elif int(age) <= 0:
             print("age is positive number")    
         else:
             break     
    
    
    while True:
        nic=input("enter your nic")
        if not nic.isdigit():
            print("nic only number")
        elif len(nic) not in [9 , 12]:
            print("NIC number 9 or 12 digit number")
        else:
            break
        
            
    account_num=acc_number_create()
    while True:
        initial_balance=float(input("enter amount"))
        if initial_balance < 0:
            print("\n amount is not negative \n")
        else:
            break    
    balance=initial_balance    

    
    user_name=name[:3].lower() + "@" + nic[-3:]
    password=input("Enter password")
    
    now=datetime.now()
    timestamp=now.strftime("%Y-%m-%d %H:%M:%S")

  
    
    customer[account_num]={
        "Name":name,
        "Age":age,
        "NIC":nic,
        "Account number_":account_num,
        "Initial_balance":  initial_balance,
        "Balance":balance,
        "User Name":user_name,
        "password":password
    
                 
        }
    
    
    with open("customer.txt","a") as file:
        file.write(f"{account_num}      {user_name}   {name}     {age}     {password}      {initial_balance}   {nic}     \n")
        print(f"sucessfuly {name} and {account_num} created account")
        
    with open("acc details.txt","a") as file:
        file.write(f"{account_num}     {user_name}      {initial_balance}      {timestamp}\n") 
    

        
        
        
# view all customer

def view_all_customers():
    try:
        
        with open("customer.txt", "r") as file:
            data = file.readlines()
        
        
        if  data:
            print("Customer Data:")
            print("accnum    name     age        password     balance      ")
            for line in data:  
                print(line.strip())  
        else:
           print("data not available")
    except FileNotFoundError:
        print("The file does not exist.")
        
#   any_one_transaction\
    
def any_one_transaction():
    acc_num=input("Enter account number")
    
    try:
        with open("transactions.txt","r")as file:
            data=file.readlines()
            if not data:
                print("NO transaction")
            for line in data:
                if line.startswith(acc_num):
                    print(line.strip())  
                    
    
    
    except FileNotFoundError:
        print("file not found")                 


  #customer login  must
def cutomer_login():
    user_name=input("enter user name")
    user_password=input("enter user password")
    
    try:
        with open("customer.txt" ,"r") as file:
            for line in file:
                data=line.strip().split()
                if len(data) >=7 :
                    cus_user=data[1]
                    cus_pass=data[4]
                    account_num=data[0]
                    if user_name ==cus_user and user_password==cus_pass :
                        print(f"Login sucessful {user_name} {account_num} welcome \n")
                        cutomer_menu(account_num)
                        return
                    else:
                        print("invalid username or password \n ")    
    
    except FileNotFoundError:
        print(" file not found.")                    
        
 #deposite
def deposit(account_num):
   
    
    try:
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount entered.")
        return

  
    updated_lines = []

    try:
        with open("acc details.txt", "r") as file:
            for line in file:
                data = line.strip().split()
                if data[0] == account_num:
                    current_balance = float(data[2])
                    new_balance = current_balance + amount
                    data[2] = str(new_balance)
                    updated_line = "  ".join(data) + "\n"
                    updated_lines.append(updated_line)
                    found = True
                else:
                    updated_lines.append(line)

        if found:
            with open("acc details.txt", "w") as file:
                file.writelines(updated_lines)

            with open("transactions.txt", "a") as file:
               
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"{account_num}  Deposit  {amount}  \n")

            print(f"Deposit successful! New balance: {new_balance}")
        else:
            print("Account number not found.")

    except FileNotFoundError:
        print("Error: acc details.txt file not found.") 
        
# withdraw    
def withdraw(account_num):
  
    try:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount entered.")
        return

    updated_lines = []


    try:
        with open("acc details.txt", "r") as file:
            for line in file:
                data = line.strip().split()
                if data[0] == account_num:  
                    current_balance = float(data[2])
                    
                    if current_balance >= amount: 
                        new_balance = current_balance - amount
                        data[2] = str(new_balance) 
                        updated_line = "  ".join(data) + "\n"
                        updated_lines.append(updated_line)
                        found = True
                    else:
                        print("Insufficient balance.")
                        return
                else:
                    updated_lines.append(line)

        if found:
            with open("acc details.txt", "w") as file:
                file.writelines(updated_lines)  

            #  transaction file
            with open("transactions.txt", "a") as t_file:
                from datetime import datetime
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                t_file.write(f"{account_num}  Withdrawal  {amount}  {now}\n")

            print(f"Withdrawal successful! New balance: {new_balance}")
        else:
            print("Account number not found.")

    except FileNotFoundError:
        print("Error: acc details.txt file not found.")    


# cutomer menu
def customer_menu(account_num):
    while True:
        print("----CUSTOMER MENU-----") 
        print("1.Deposit Money") 
        print("2.Withdraw money") 
        print("3.exit") 
        
        choice=input("Enter choice 1-3")
        if choice=="1":
            deposit(account_num)
        elif choice =="2":
             withdraw(account_num)
        
        elif choice=="3":
            break
        else:
            print("invalid choice")
        
            
         
          
#admin menu
def admin_menu():
    while True:
        print("****Admin Menu****")
    
        print("1.account create")
        print("2.view all customer")
        print("3.any_one_transaction")
        
        print("4.exit")
        
        
        choice=input("Enter Choice")
        if choice =='1':
            account_create()
        elif choice == "2":
           view_all_customers()
        elif choice == "3":
            any_one_transaction()
        elif choice =="4":
            break    
        else:
            print("Invalid choice")
        




def menu():

     while True:

        print("\n --------MINI BANKING SYSTEM --------\n")
        print("1. Admin Login")
        print("2. Customer Login")
        print("3. Exit")

        choice =input("input choice: ")
        if choice == "1":
            check_admin()
        
        elif choice == "2":
            cutomer_login()
        
        elif choice == "3":
            break
        else:
            print("Invalid choice..")

menu()