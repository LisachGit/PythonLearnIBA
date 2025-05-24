import math
import time

class SinusIterableWithGenerator:
    def __init__(self, steps, width):

        self.steps = steps
        self.width = width

    def __iter__(self):
        x = 0.0
        while True:
            x += math.pi * 2 / self.steps
            length = self.width / 2 + self.width / 2 * math.sin(x) + 1
            yield '#' * int(length)

if __name__ == '__main__':
    main_iter = SinusIterableWithGenerator(32, 10)
    for line in main_iter:
        print(line)
        # задержка между выводами
        time.sleep(0.25)