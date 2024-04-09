class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Man(Human):
    def __init__(self, name, age):
        super().__init__(name, age)

class Woman(Human):
    def __init__(self, name, age):
        super().__init__(name, age)

def create_adam_and_eve():
    adam = Man("Adam", age=30)
    eve = Woman("Eve", age=28)
    return [adam, eve]

# Test the creation method
adam_and_eve = create_adam_and_eve()
for person in adam_and_eve:
    print(f"{person.name} is {person.age} years old.")
