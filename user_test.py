import unittest #import the unittest module
from user import User #import the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases.
    '''
    # First test
    def setUp(self): #setup() creates new instances  of the user class before each test method declared. it is called before invocation of the test.
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Maratah","Njoroge","1234r54","maratah7@gmail.com") # instance variable are stored here

   
    def test_init(self): #checks if objects are initialised correctly
        '''
        test_init test case to test if the object is initialized properly
        '''

        #check for an expected result
        self.assertEqual(self.new_user.first_name,"Maratah") 
        self.assertEqual(self.new_user.last_name,"Njoroge")
        self.assertEqual(self.new_user.password,"1234r54")
        self.assertEqual(self.new_user.email,"maratah7@gmail.com")

    #second test
    def test_save_user(self):
        '''
        test_save_user test case to test if the contac object is saved into the contact list
        '''
        self.new_user.save_user() #save new user
        self.assertEqual(len(User.user_list),1) #check length to confirm new addition to the user list


    #third test
    def test_save_multiple_user(self):
        '''
        test_save_multiple_user checks if we can save multiple user info to our user list
        '''
        self.new_user.save_user()
        test_user = User("Test","user","123456723","test@user.com")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)


    def tearDown(self): #called  after invocation of each test method 
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = [] #to get accurate  test results every time a new test case

#forth test
    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from the user list.
        '''
        self.new_user.save_user()
        test_user= User("Test", "user","123456778", "test@user.com")
        test_user.save_user()
        self.assertEqual(len(User.user_list),1)
   
  

#fifth test

    def test_find_user_by_name(self):
        '''
        test to check if we can find a user by their name and display the info.
        '''
        self.new_user.save_user()
       
        test_user= User("Test","user","1235t6","test@user.com")
      
        test_user.save_user()
        
        found_user = User.find_by_name("User")
 
        self.assertEqual(found_user.email,test_user.email)
        
    
    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("Test","user","0711223344","test@user.com") # new contact
        test_user.save_user()

        user_exists = User.user_exist("0711223344")

        self.assertTrue(user_exists) #checks if the return value is true
 
  
    def test_display_all_user(self):
        '''
        Method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(),User.user_list)

if __name__ == '__main__': #confirm that anything inside the if block should run only if the file is being run
    unittest.main() #command line interface
