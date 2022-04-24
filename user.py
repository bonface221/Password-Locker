class User:
    user_list =[]
    def __init__(self,first_name,last_name, user_name,password):
        self.fist_name =first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password= password
        

    def save_user(self):
        User.user_list.append(self)

    @classmethod
    def find_user_by_username(cls,name):
        for user in cls.user_list:
            if user.user_name ==name:
                return True
        
        return False

    @classmethod 
    def find_user_by_password(cls, password):
        for user in cls.user_list:
            if user.password == password:
                return True
        
        return False
        

    