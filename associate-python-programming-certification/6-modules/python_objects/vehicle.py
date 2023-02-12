class Vehicle:
    """
    Vehicle models a vehicle w/ tires and an engine
    """

    default_tire = 'tire'

    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires

    def description(self):
        print(f"A vehicle with an {self.engine} engine, and {self.tires} tires")

    @classmethod
    def bicycle(cls, tires=None):
        if not tires:
            tires = [cls.default_tire, cls.default_tire]
        return cls(None, tires)

civic = Vehicle('4-cylinder', ['front-driver', 'front-passenger', 'rear-driver', 'rear-passenger'])
print(civic.description())
print(Vehicle.default_tire)
bycicle = Vehicle.bicycle()
print(bycicle.tires)
bycicle.description()
