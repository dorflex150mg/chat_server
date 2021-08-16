class Users:

    
    #TODO: init with nothing. Create new users
    def __init__(self):
        self.users = set(["fren"])
        self.users.add("other_fren")

    def sign_up(self, user_id):
        self.users.add(user_id)
        
    def check_registered_users(self, user):
        return user in self.users
            
