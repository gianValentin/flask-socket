class User:

    def __init__(self,id = 0,username = "",password = ""):
        self.id = id
        self.username = username
        self.password = password

    def json(self):
        json = {"id":str(self.id),"username":self.username,"password":self.password}
        print(json)
        return json
    
    def setId(self,id):
        self.id = id
    
    def getId(self):
        return self.id

    def setUsername(self,username):
        self.username = username
    
    def getUsername(self):
        return self.username
    
    def setPassword(self,password):
        self.password = password
    