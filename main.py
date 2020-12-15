from person import Person

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948", "Jordan")
print(sonny.name, sonny.email, sonny.phone)

jordan = Person("Jordan", "jordan@aol.com", "495-586-3456", "Sonny")
print(jordan.name, jordan.email, jordan.phone)

sonny.greet(jordan)


sonny.print_contact_info()

jordan.friends.append(sonny) 
sonny.friends.append(jordan)

print(sonny.friends)
print(jordan.friends)
