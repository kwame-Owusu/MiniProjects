from cryptography.fernet import Fernet


#all the code was coded along from tech with tim youtube channel go check it out for further explanation.


master_pwd = input("What is the master password: ")

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key) '''

def load_key():
    file =  open("key.key","rb")
    key = file.read()
    file.close
    return key




def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "Password:",passw)

        


def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("password.txt", "a") as f: 
         f.write(name + "|" + pwd + "\n")


    

while True:
    
    mode = input("Would you like to add a new password or view existing ones (view, add)? ")
    
    if mode == "q":
        break
    
    if mode == "view": 
        view()
    elif mode == "add":
        add()

    else:
        print("Invalid mode.")
        continue


