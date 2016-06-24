class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def drive_car(self):
        self.condition="used"
        return self.condition
    def display_car(self):
        return 'This is a %s %s with %s MPG.' % (self.color, self.model, str(self.mpg))

my_car = Car("Maruthi", "silver", 88)

print(my_car.condition)
print(my_car.model)
print(my_car.color)
print(my_car.mpg)
print(my_car.drive_car())
print(my_car.display_car())