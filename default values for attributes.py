class User:
      def __init__(self, userId, userName):
            self.id = userId
            self.name = userName
            self.followers = 0
            self.following = 0
            
      def follow(self, user):
            user.followers += 1
            self.following += 1
            
user1 = User(101, "krishvi")
user2 = User(102, "heena")
user2.follow(user1)
print(user1.name, user1.followers, user1.following)
print(user2.name, user2.followers, user2.following)
