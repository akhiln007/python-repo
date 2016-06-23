class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health="good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!

    def description(self):
        print(self.name)
        print(self.age)

hippo=Animal("Hippy",10)
sloth=Animal("Test_Sloth",20)
ocelot=Animal("Test_Ocelot",30)
hippo.description
print(hippo.health)
print(sloth.health)
print(ocelot.health)