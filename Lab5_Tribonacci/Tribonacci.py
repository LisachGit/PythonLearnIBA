class Tribonacci:
    def __init__(self, n):
        self.count = n
    def __iter__(self):
        return self.generator()
    def generator(self):
        x,y,z = 0,1,1
        for _ in range(self.count):
            yield x
            x,y,z = y,z,x+y+z

if __name__ == '__main__':
    tribonacci_iterable = Tribonacci(35)
    print("Последовательность Трибоначчи: ")
    for i in tribonacci_iterable:
        print(i)
