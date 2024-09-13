# Day 17 of 100 days Of Python Bootcamp

# Creating a Class

class User:
    # make sure to make first character of your class name capital
    #pass
    #constructor
    # whenever a new object is created parameters must be passed, init confirmed this.
    def __init__(self,user_id,user_name):
        #print("new user login!")
        # to assign attribute a value
        self.id=user_id
        self.name=user_name
        # we can also provide default value
        self.follower=0
        self.following=0

    # when a function is attached to an object it's called method.
    def follow(self,user):
        user.follower +=1
        self.following +=1



user_1=User("801","Utkarsh")

# attribute is a variable that associate with object.
# attributes are things that object will have.
# methods are the things that object does. i.e. just like functions
#user_1.id="801"
#user_1.username='angela'

print(user_1.id,user_1.follower)

user_2=User("802","Ayush")
#user_2.id="802"
#user_2.username='utkarsh'

user_1.follow(user_2)
user_2.follow(user_1)
print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)




