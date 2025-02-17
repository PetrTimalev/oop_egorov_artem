class AverageAccumulator:
    def __init__(self):
        self.data = []

    def __call__(self, new_value):
        self.data.append(new_value)
        return sum(self.data) / len(self.data)


avg = AverageAccumulator()
print(avg(10))
print(avg(20))
print(avg(30))