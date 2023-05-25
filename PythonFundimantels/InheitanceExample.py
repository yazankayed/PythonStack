class Vehicles:
    def __init__(self,name,color,Price):
        self.name=name
        self.color=color
        self.price=Price

class Car(Vehicles):
    def __init__(self, name, color, Price,maxspeed):
        super().__init__(name, color, Price)
        self.maxSpeed=maxspeed

ford=Car("Ford","Blue",50000,180)

print(ford.name)
print(ford.color)
print(ford.price)
print(ford.maxSpeed)