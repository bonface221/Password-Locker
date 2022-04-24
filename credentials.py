import random
class Credentials:
    
    credentials_list = []
    '''
    __init__ method that helps us define properties for our objects.
    '''
    def __init__(self,user_name,social_platform,password):
        self.user_name =user_name
        self.social_platform =social_platform
        self.password = password

    '''
    function to generate a random unhackable password using 
    the random sample method
    '''
    def generate_password(self,pass_length=8):
        lower_case = 'abcdefghijklmnopqrstuvwxyz'
        upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        number= '1234567890'
        symbols = '~!@#$%^&*()+?/|'

        use_password = lower_case+ upper_case + number + symbols

        password = ''.join(random.sample(use_password,pass_length))
        return password

    '''
    method to save the logins by appending to the credentials list
    '''
    def save_login_credentials(self):
        Credentials.credentials_list.append(self)

    '''
    method to delete the credentials by looping through the credentials list
    '''
    @classmethod
    def delete_credentials(cls,social):
        for credential in cls.credentials_list:
            if credential.social_platform ==social:
                Credentials.credentials_list.remove(credential)  
                return  
    '''
    method to check whether a certain credential is present
    '''
    @classmethod
    def credential_exist(cls, social):
        for credential in cls.credentials_list:
            if credential.social_platform == social:
                return True

        return  False

    '''
    method to find the individual credentials 
    '''
    @classmethod
    def find_by_name(cls,social):
        for credential in cls.credentials_list:
            if credential.social_platform == social:
                return credential

    '''
    method to display all the available credentials stored
    '''

    @classmethod
    def display_credential(cls):
        return cls.credentials_list