class Car():
    def __init__(self,name,module,year):
        self.name = name
        self.module = module
        self.year = year
    def car_info(self):
        car_info = f'{self.name} {self.module} {self.year}'
        print (car_info.title())