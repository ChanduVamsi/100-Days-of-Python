'''
Naming conventions in python:
1. Classes = PascalCase
2. Methods = camelCase
3. Attributes = snake_case
4. Constants = UPPERCASE
'''

class User:
    username = ""
    id = 1
    followers = 0
    following = 0

    def __init__(self, username) -> None:
        print("New user being created")
        self.username = username
        self.id = self.id
        User.id += 1

    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User("Chandu")
user2 = User("Vamsi")
user3 = User("Mr X")

user1.follow(user2)
user1.follow(user3)

for user in [user1, user2, user3]:
    print(user.username, user.id, user.followers, user.following)
