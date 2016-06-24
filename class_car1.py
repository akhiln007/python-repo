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

class ElectricCar(Car):
    def __init__(self,model,color,mpg,battery_type):
        Car.__init__(self,model,color,mpg)
        self.battery_type=battery_type
    def drive_car(self):
        self.condition="like new"
    

my_car=ElectricCar("Ford","Silver","06","molten salt")
print(my_car.condition)
print(my_car.drive_car())
print(my_car.condition)