class God:
    def __init__(self):
        self.adam_and_eve = self.create_adam_and_eve()

    def create_adam_and_eve(self):
        adam = Man("Adam")
        eve = Woman("Eve")
        return [adam, eve]

    def __getitem__(self, index):
        return self.adam_and_eve[index]

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
