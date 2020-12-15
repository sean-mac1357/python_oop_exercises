from person import Person

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
print(sonny.name, sonny.email, sonny.phone)

jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
print(jordan.name, jordan.email, jordan.phone)

sonny.greet(jordan)

sonny.print_contact_info()

jordan.add_friend(sonny)
sonny.add_friend(jordan)

print(len(jordan.friends))

sonny.greet(jordan)
sonny.greeting_count

print(sonny.greeting_count)
print(jordan.greeting_count)

print(str(jordan))
print(str(sonny))