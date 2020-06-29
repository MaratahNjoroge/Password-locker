class Credential:
    """
    Class that generates new instances of credentials.
    """

    credential_list = []

    def __init__(self,credential_name,user_name,password,email):
        
        self.credential_name = credential_name
        self.user_name = user_name
        self.password = password
        self.email = email

    def save_credential(self):

        '''
        save_credetial method saves credential objects into credential_list
        '''

        Credential.credential_list.append(self)

    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self)


    @classmethod
    def find_by_name(cls,name):
        '''
        Method that takes in a name and returns a credential that matches that name.

        Args:
            name: Credetial to search for
        Returns :
            Credetial of person that matches the name.
        '''

        for credential in cls.credential_list:
            if credential.credential == name:
                return credential

    @classmethod
    def credential_exist(cls,name):
        '''
        Method that checks if a credential exists from the credentials list.
        Args:
            name: User name to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.password == name:
                    return credential

        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list