class User:
    '''
    Class that generates new instances of contacts
    '''

    user_list = []

    '''
    __init__ method that helps us define properties for our objects.
    '''

    def __init__(self, first_name, last_name, user_name, password):
        self.fist_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password

    '''
    method to append users to the user list
    '''

    def save_user(self):
        User.user_list.append(self)

    '''
    method to find users by the name for validation purposes
    '''
    @classmethod
    def find_user_by_username(cls, name):
        for user in cls.user_list:
            if user.user_name == name:
                return True

        return False

    '''
    method to validate a user using the password find
    '''
    @classmethod
    def find_user_by_password(cls, password):
        for user in cls.user_list:
            if user.password == password:
                return True

        return False
