import os

#admin checking
def check_admin():
 
    if not os.path.exists("admin_account.txt"):
        print("No admin account\n plese create one")
        create_admin()
    else:
        admin_login()    


#admin create
def create_admin():

    ad_username=input("--Ender admin user name---")
    ad_password=input("--Ender admin password--")

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
            last_acc_num = last_line.split()[2]  
            last_num = int(last_acc_num.replace("ACC", ""))
            return f"ACC{last_num + 1:03}"
    except FileNotFoundError:
        return "ACC001"



#account create

def account_create():
    customer={}
    name=input("enter name")
    age=input("enter age")
    account_num=acc_number_create()
    initial_balance=float(input("enter amount"))
    user_name=input("enster user name"),
    password=input("Enter password")
    # user_id=input("enter id")
    
    customer[account_num]={
        "Name":name,
        "Age":age,
        "Account number_":account_num,
        "Initial_balance":  initial_balance,
        "User Name":user_name,
        "password":password
    
                 
        }
    
    with open("cutomer.txt","a") as file:
        file.write(f"{name}{age:<5}{account_num:<5}{initial_balance:<5}{user_name:<5}{password:<5}\n")
        print(f"sucessfuly {name} and {account_num} created account")
        
        
        
# view all customer

def view_all_customers():
    
    with open("custmoer.txt","r") as file:
        customer=file.read()
        if customer:
            for account_num, customer_details in customer:
                print(f"acc num:{account_num}, details:{customer_details}")
                
        else:
            print("file not found")        
            
 
            
        
        
      
        
 
 
 
 
 #customer login

    
      
        
 

 
        
        
            
#admin menu
def admin_menu():
    while True:
        print("****Admin Menu****")
    
        print("1.account create")
        print("2.view all customer")
        print("3.exit")
        
        
        choice=input("Enter Choice")
        if choice =='1':
            account_create()
        elif choice == "2":
           view_all_customers()
        elif choice == "3":
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
            pass
        
        elif choice == "3":
            break
        else:
            print("Invalid choice..")

menu()