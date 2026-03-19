class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def showSpeed(self):
        print("Speed:", self.speed)


class Car(Vehicle):
    def __init__(self, speed, brand):
        super().__init__(speed)
        self.brand = brand

    def display(self):
        self.showSpeed()
        print("Brand:", self.brand)


c1 = Car(120, "renge rover")
c1.display()