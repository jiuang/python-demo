class Fruit:
    def grow(self):
        print("Fruit grow", self)


class Apple(Fruit):
    def grow(self):
        Fruit.grow(self)
