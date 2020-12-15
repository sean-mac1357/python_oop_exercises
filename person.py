class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))


sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
print(sonny.name, sonny.email, sonny.phone)

jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
print(jordan.name, jordan.email, jordan.phone)

sonny.greet(jordan)
print(sonny.name, sonny.email, sonny.phone)
