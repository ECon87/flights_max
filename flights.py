
from operator import itemgetter

class Flights():

    def __init__(self):
        self.flights = []
        self.maxflights = {}
        return

    def add_flight(self, flight: list[int]):
        self.flights.append(flight)

    def max_flights_air(self):
        for i in range(1, 25):
            self.maxflights[i] = 0
            for f in self.flights:
                if f[0] <= i <= f[1]:
                    self.maxflights[i] += 1
        return max(self.maxflights.values())


# Example

example = Flights()
print(example.maxflights)
print(example.flights)
example.add_flight([1, 5])
example.add_flight([2, 6])
example.add_flight([8, 14])
example.add_flight([7, 11])
example.add_flight([10, 12])
example.add_flight([11, 12])
print(example.flights)
example.max_flights_air()
print(example.maxflights)

