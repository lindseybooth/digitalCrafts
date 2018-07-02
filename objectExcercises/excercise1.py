class Person: 
    def __init__(self, name, email, phone): 
        self.name = name 
        self.email = email 
        self.phone = phone 
        self.friends = []
        self.greeting_count = 0

    def contactInfo(self):
        return "Name: {} Email: {} Phone {}".format(self.name, self.email, self.phone)

    def greet(self, other_person): 
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1
        

    def add_friend(self, friend):
        return self.friends.append(friend.name)
        

    def num_of_friends(self):
        print(len(self.friends))

    def __str__(self): 
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)

person1 = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
person2 = Person("Jordan", "jordan@aol.com", "495-586-3456")

person1.add_friend(person2)
person2.add_friend(person1)

person1.num_of_friends()
person2.num_of_friends()

person1.add_friend(person2)
person2.add_friend(person1)

person1.greet(person2)
person2.greet(person1)

print(person1.greeting_count)

print(person1.contactInfo())
print(person2.contactInfo())
