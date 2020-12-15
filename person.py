class Person:
    def __init__(self, name, email, phone, friends):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))

    def print_contact_info(self):
        print("{}'s email: {}".format(self.name, self.email))
        print("{}'s phone number: {}".format(self.name, self.phone))

    def add_friend(self, other_person):
        self.friends.append(other_person)
        print("{}'s friends are: {}".format(self.name, other_person.name))

