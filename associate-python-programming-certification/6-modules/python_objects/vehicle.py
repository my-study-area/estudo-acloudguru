class Vehicle:
    """
    Vehicle models a vehicle w/ tires and an engine
    """

    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires

    def description(self):
        print(f"A vehicle with an {self.engine} engine, and {self.tires} tires")
