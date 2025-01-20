class Car:
    def __init__(self, engine):
        self.engine = engine
    def start(self):
        self.engine.start()
class Engine:
    def start(self):
        print("engine starting.......")

car = Car(Engine())
car.start()
