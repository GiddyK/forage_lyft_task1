from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery, tires):
        self.engine = engine
        self.battery = battery
        self.tires = tires

    def needs_service(self):
<<<<<<< HEAD
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()
=======
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()
>>>>>>> 1767c3c (lyft virtual experience programm)
