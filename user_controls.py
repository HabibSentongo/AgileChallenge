import datetime

class UserConcerns:
    def __init__(self,username=None,password=None,database=None):
        self.username=username
        self.password=password
        self.date=\
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.database=[]

    def create_user(self,username,password):
        input_username=input("Type your username here: ")
        input_password=input("Your password please: ")
        self.one_user={
            'username':input_username,
            'password':input_password}
        if len(input_username)< 5:
            response_object='Please make your username a bit longer'
            return response_object
        elif len(input_password)< 5:
            response='make the password longer than 5 characters'
            return response
        else:
            self.database.append(self.one_user)
            return ('{0}\'s account has successfully\
             been created'.format(self.username))

    def login_user(self,username,password):
        input_username=input("Type your username here: ")
        input_password=input("Your password please: ")
        self.one_user={
            'username':input_username,
            'password':input_password
            }
        for user in self.database:
            if (input_username,input_password) == (
                user[username],user[password]
                ):
                message= "{0} is now logged in at {1}".format(input_username,self.date)
                response_object={'message':message}
                return response_object
            else:
                response_object="invalid login credentials"
                return response_object

if __name__ == "__main__":
    UserConcerns().create_user()
    UserConcerns().login_user()