class God:
    @staticmethod
    def create_adam_and_eve():
        adam = Man("Adam")
        eve = Woman("Eve")
        return [adam, eve]

class Human:
    pass

class Man(Human):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} is a man"

class Woman(Human):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} is a woman"

# Test the creation method
adam_and_eve = God.create_adam_and_eve()
for person in adam_and_eve:
    print(person)
