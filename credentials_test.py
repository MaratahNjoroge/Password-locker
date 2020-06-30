import unittest
from credentials import Credential

class TestCredential(unittest.TestCase):

    def setUp(self):
        '''
        Set up to run each test case.
        '''
        self.new_credential = Credential("Maratah","iamnjoroge","1234r54", "maratah7gail.com")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        
        self.assertEqual(self.new_credetial.credential_name,"Maratah")
        self.assertEqual(self.new_credential.user_name,"iamnjoroge")
        self.assertEqual(self.new_credential.password,"1234r54")
        self.assertEqual(self.new_credential.email,"maratah7@gmail.com")


    def test_save_credential(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_credential.save_credential() # saving the new contact
        self.assertEqual(len(Credential.credential_list),1)


    def test_save_multiple_credential(self):
            '''
            test_save_multiple_credential to check if we can save multiple credential
            objects to our credential_list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("Test","user","34253t766","test@user.com") # new contact
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credential.credential_list = []


    def test_delete_credential(self):
            '''
            test_delete_credential to test if we can remove a contact from our contact list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("Test","user","0712345678","test@user.com") # new contact
            test_credential.save_credential()
            self.new_credential.test_delete_credential()# Deleting a contact object
            self.assertEqual(len(Credential.credtial_list),1)   


    def test_find_credential_by_name(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credential("Test","user","0711223344","test@user.com") # new contact
        test_credential.save_credential()

        found_credential = Credential.find_by_name("Test")

        self.assertEqual(found_credential.email,test_credential.email)  


    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential.
        '''

        self.new_credential.save_credential()
        test_credential = Credential("Test","user","0711223344","test@user.com") # new contact
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("0711223344")

        self.assertTrue(credential_exists)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credential.display_credentials(),Credential.credential_list)
      
          
if __name__ == '__main__':
    unittest.main()
