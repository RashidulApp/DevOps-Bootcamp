
"""
User Atributes

Name: 
Email:
Password:
Job Title:

User Behavior

changePassword()
changeJobTitle()
displayUserInfo()


"""


class User:
    def __init__(self, name, email, password, jobTitle ):
        self.name = name
        self.email = email
        self.password = password
        self.jobTitle = jobTitle

    def changePassword(self, password):
        self.password = password

    def changeJobTitle(self, jobTitle):
        self.jobTitle = jobTitle

    def displayUserInfo(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Job Title: {self.jobTitle}")

user1 = User("Rashidul", "r@gmail.com", "pwd", "DevSecOps")
user2 = User("Shakira", "s@gmail.com", "pwd", "House Wife")
user1.displayUserInfo()
user2.displayUserInfo()
user1.changePassword("change")
user1.changeJobTitle("DevOps")
user1.displayUserInfo()

