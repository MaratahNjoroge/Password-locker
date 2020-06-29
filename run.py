#!/usr/bin/env python3.6
from user import User
from credentials import Credential



def create_user(fname,lname,password,email): #create new user account
    '''
    Function to create a new user 
    '''
    new_user = User(fname,lname,password,email)
    return new_user

def save_users(user): #save the user info
    '''
    Saves the users info
    '''
    user.save_user()

def del_user(user): #delete the user info
    '''
    Delete user info
    '''
    user.delete_user()

def find_user(name): #find user
    '''
    Find user by name and return the user info
    '''
    return User.find_by_name(name)


def check_existing_users(name): #check if info exists
     '''
     check if user info exists and return a Boolean
     '''
     return User.user_exist(name)

def display_users():
    '''
    display user info
    '''
    return User.display_users()


#___credentials


def create_credential(fname,lname,password,email): #create new user account
    '''
    Function to create a new credential 
    '''
    new_credential = Credential(fname,lname,password,email)
    return new_credential

def save_credentials(user): #save the user info
    '''
    Saves the credentials info
    '''
    credential.save_credentials()

def del_credential(credential): #delete the user info
    '''
    Delete user info
    '''
    credential.delete_credential()

def find_credential(name): #find user
    '''
    Find credential by name and return the credential info
    '''
    return Credential.find_by_name(name)


def check_existing_credentials(password): #check if info exists
     '''
     check if user credentials exists and return a Boolean
     '''
     return Credential.credential_exist(password)

def display_credentials():
    '''
    display user credential
    '''
    return Credential.display_credentials()

#main function this will be the base for interaction between the frotend and backend
#user_________
def main():
    print("Bonjour! Welcome to the user password locker app. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. sign up to to create an account.")
    print('\n')

    while True:
                    print("Use these short codes :SU - Sign up, du - display user info, LG-Log in, ex -exit the password locker ")

                    short_code = input().lower()

                    if short_code == 'su':
                            print("Create a Password locker account")
                            print("-"*10)

                            print ("User name  ....")
                            user_name = input()

                            print("Account name ...")
                            account_name = input()

                            print("Password ...")
                            password = input()

                            print("Email address ...")
                            e_address = input()


                            save_users(create_user(user_name,account_name,password,e_address)) # create and save new contact.
                            print ('\n')
                            print(f"New Account {user_name} {account_name} created")
                            print ('\n')

                    elif short_code == 'du':

                            if display_users():
                                    print("Here is a account and all your details")
                                    print('\n')

                                    for user in display_users():
                                            print(f"{user.user_name} {user.account_name} .....{user.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any  saved account.Please sign up to create a new account. ")
                                    print('\n')

                    elif short_code == 'LG':
                            print("Enter your password to log in")
                            search_user = input()
                            if check_existing_users(search_user):
                                    search_user = find_user(search_user)
                                    print(f"{search_user.user_name} {search_user.account_name}")
                                    print('-' * 20)

                                    print(f"You are logged in to your{user_name}")
                                  
#credentials_________
                            while True:
                                print("Use these short codes:CA - Create new credential.DC - Display your credentials list ex -Log out your credentials account.")
                                
                                short_code = input().lower()
                                
                                if short_code == "ca":

                                    print("Create new credential")
                                    print('_' * 20)

                                    account_name = input('Credential of Social media Name:')
                                    print('\n')

                                    user_name = input(f"{user_name} user name:")
                                    print('\n')
                                    print('*' * 20)

                                    password = input(f"{user_name} password:")
                                    save_credentials((account_name,user_name,password,e_address))                                    
                                    print('\n')
                                    
                                    print(f"A New {account_name} Account with the user name  {user_name} has been created.")
                                   
                                    print ('\n')
                                
                                elif short_code == 'dc':
                                    
                                    if display_credentials():
                                       
                                        print("Here is your credentials")
                                       
                                        print('\n')
                                       
                                        for credentials in display_credentials():
                                       
                                            print(f"Credential name:{credentials.credentials_name}  User name: {credentials.usr_name} Password:{credentials.password}")
                                       
                                            print('\n')
                                    
                                    else:
                                        print('\n')
                                        print("You don't seem to have created any account yet")
                                        print('\n')

                                elif short_code == "ex":
                                    print('\n')
                                    print(f"You have logged out your {user_name} account")
                                    print('\n')
                                    break
                                  
                                    
                                                                                                                                                                                                                                                                       
                            else:
                                    print("That account does not exist")

                    elif short_code == "ex":
                            print("Thank you {user_name}. Hope you enjoyed the service. Goodday .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
    main()              
