import pyperclip
class User:
    """
    Class that generates new instances of users

    """

    user_list = [] #pass in an empty array to my user_list variable displaying an empty user info

    def __init__(self,first_name,last_name,password,email):


#created instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email

    def save_user(self):

        '''
        save user method save user objects into user_list
        '''

        User.user_list.append(self) #the append method modifies the orignal list by adding a new user to the original list.

    def delete_user(self):
        '''
        delete_user method will delete a saved user info from the user_list.
        '''
        User.user_list.remove(self) # remove method deletes the user info from the user list  

    @classmethod  #the decorator informs the interpreter that the othod belongs to the entire class
    def find_user_by_name(cls,name): #the find_by_nama loops through each user object in the user_list and check if the name equals the name passed.
        '''
        Takes in a name and returns a user that matches that name.
        Args:
            name: User name to seach for
        Returns : 
            Account info of user that matches the name.
        '''

        for user in cls.user_list:
            if user.name == name:
                return user

    @classmethod #loops through all the saved user info and checks if any matches the name passed in.
    def user_exist(cls,name):
        '''
        Method that checks if a user exists from the user list.
        Args:
            name: User name to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.name == name:
                    return True

        return False 

    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list  
    
    @classmethod
    def copy_email(cls,name):
        found_user = User.find_by_name(User)
        pyperclip.copy(found_user.email)