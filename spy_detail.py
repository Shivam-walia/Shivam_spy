#import or add datetime
from datetime import datetime

#spy class is defined
class Spy:

#function defination with constructor
    def __init__(self, name, salutaton, age, rating):
        self.name = name
        self.salutaton = salutaton
        self.age = age
        self.rating = rating
        self.online = True
        self.chats = []
        self.current_status_message = None
#function defination for another class
class chat_message:

    def __init__(self,message,sent_by_me):
        self.message=message
        self.time=datetime.now()
        self.sent_by_me=sent_by_me


spy=Spy('Shivam','Mr.',21,4.4)

friend_one=Spy('Radhe','Mr.',20,4.2)
friend_two=Spy('satya','Mr.',23,4.3)
friend_three=Spy('Puri','Mr.',22,4.5)
friend_four=Spy('Kullu','Mr',21,4.3)

friends=[friend_one,friend_two,friend_three,friend_four]



