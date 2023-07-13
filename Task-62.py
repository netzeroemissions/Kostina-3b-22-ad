class Robot:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def distance(self, time):
        return time * self.speed

class CrawlerRobot(Robot):
    def __init__(self, name, speed, territory):
        super().__init__(name, speed)
        self.territory = territory

class WheelRobot(Robot):
    def __init__(self, name, speed, car_brand):
        super().__init__(name, speed)
        self.car_brand = car_brand

robot = Robot('Ivan', 3)
crawler = CrawlerRobot('Worm', 5, 'Ilya')
cart = WheelRobot('Basket', 15, 'Anna')
print(robot.distance(5))
print(crawler.distance(4))
print(cart.distance(7))
print(crawler.territory)
print(cart.car_brand)