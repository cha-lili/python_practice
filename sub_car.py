from car import Car

class Sub_Car(Car):
    def __init__(self,name,module,year):
        super().__init__(name,module,year)
        self.battery = 70

    def battery_size(self):
        message = f'This car has a {self.battery} -KWh battery'
        print (message)
