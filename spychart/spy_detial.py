from datetime import datetime
class Spy:

    #The function __init__() is a constructor.
    def __init__(self, name, salutation, age, rating):

        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None
# ChatMessage class.
class ChatMessage:

    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me
#Using the class definition of Spy, let's create our own spy.
spy = Spy('bond', 'Mr.', 24, 4.7)

friend_one = Spy('Raja', 'Mr.', 27, 4.9)
friend_two = Spy('Mata Hari', 'Ms.', 21, 4.39)
friend_three = Spy('No', 'Dr.', 37, 4.95)

friends = [friend_one, friend_two, friend_three]

