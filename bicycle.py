class Bicycle(object):
    counter = 0

    def __init__(self, number_of_gears=21, weight=15, max_weight=100, producer="PaPa", model="PoSH", tire_size=26,
                 frame_size=12.5):
        Bicycle.counter += 1
        self.number_of_gears = number_of_gears
        self.weight = weight
        self.max_weight = max_weight
        self.producer = producer
        self.model = model
        self.tire_size = tire_size
        self.frame_size = frame_size

    def __del__(self):
        print(self.model + ' R. I. P.')

    def __str__(self):
        return 'Bicycle(number_of_gears=' + str(self.number_of_gears) + ', weight=' + str(
            self.weight) + ', max_weight=' + str(
            self.max_weight) + ', producer=' + self.producer + ", model=" + self.model + ', frame_size=' + str(
            self.frame_size) + ', tire_size=' + str(self.tire_size) + ')'

    @staticmethod
    def get_counter():
        return Bicycle.counter


if __name__ == '__main__':
    bicycle_a = Bicycle(number_of_gears=28, weight=22, max_weight=150, producer="DDD", model="dwarf", frame_size=18,
                        tire_size=10)
    print(bicycle_a)
    print(Bicycle.get_counter())
    bicycle_b = Bicycle()
    print(bicycle_b)
    print(Bicycle.get_counter())
    bicycle_с = Bicycle(number_of_gears=47, weight=50, max_weight=1000, producer="FFF", model="WTF")
    print(bicycle_с)
    print(Bicycle.get_counter())
