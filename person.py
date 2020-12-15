class Person:
    def __init__(self, name, email, phone, friends):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count =+ 1
        print("{}'s greeting count is: {}".format(self.name, self.greeting_count))

    def print_contact_info(self):
        print("{}'s email: {}".format(self.name, self.email))
        print("{}'s phone number: {}".format(self.name, self.phone))

    def add_friend(self, new_friend):
        self.friends.append(new_friend)
        print("{}'s friends are: {}".format(self.name, new_friend.name))
    

