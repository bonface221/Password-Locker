import random
class Credentials:
    
    credentials_list = []

    def __init__(self,user_name,social_platform,password):
        self.user_name =user_name
        self.social_platform =social_platform
        self.password = password

    
    def generate_password(self,pass_length=8):
        lower_case = 'abcdefghijklmnopqrstuvwxyz'
        upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        number= '1234567890'
        symbols = '~!@#$%^&*()+?/|'

        use_password = lower_case+ upper_case + number + symbols

        password = ''.join(random.sample(use_password,pass_length))
        return password

    def save_login_credentials(self):
        Credentials.credentials_list.append(self)
    @classmethod
    def delete_credentials(cls,social):
        for credential in cls.credentials_list:
            if credential.social_platform ==social:
                Credentials.credentials_list.remove(credential)  
                return  

    @classmethod
    def credential_exist(cls, social):
        for credential in cls.credentials_list:
            if credential.social_platform == social:
                return True

        return  False

    @classmethod
    def find_by_name(cls,social):
        for credential in cls.credentials_list:
            if credential.social_platform == social:
                return credential

    @classmethod
    def display_credential(cls):
        return cls.credentials_list