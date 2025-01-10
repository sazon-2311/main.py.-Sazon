class Figure:
    sides_count = 0
    __sides = []
    __color = []
    filled = False

    def __init__(self, rgb, *side):
        self.sides = None
        self.color = list(rgb)
        self.side = side[0]
        self.filled = True

    def get_color(self):
        self.__color = self.color
        self.filled = True
        return self.__color

    def _is_valid_color(self, r, g, b):
        self.r, self.g, self.b = r, g, b
        if 0 <= self.r <= 255 and 0 <= self.g <= 255 and 0 <= self.b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self.color = [self.r, self.g, self.b]

    def _is_valid_sides(self, *sides):
        for side in self.sides:
            if isinstance(side, int) and len(self.sides) == self.sides_count:
                return True
            else:
                return False

    def get_sides(self):
        self.__sides = self.sides
        return self.__sides

    def set_sides(self, *new_sides):
        massive = []
        self.sides = list(new_sides)
        if self._is_valid_sides(self, *new_sides):
            self.get_sides()
        else:
            for i in range(self.sides_count):
                massive.append(self.side)
            self.sides = massive
            self.get_sides()

    def __len__(self):
        return self.sides[0] * self.sides_count


class Circle(Figure):
    sides_count = 1
    __radius = None

    def set_radius(self):
        self.__radius = self.__len__() / (2 * 3.141569)
        return self.__radius

    def get_square(self):
        self.set_radius()
        return (self.__radius ** 2) * 3.141569


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a = self.get_sides()[0]
        return (a ** 2 * 3) ** 0.5 / 2


class Cube(Figure):
    sides_count = 12

    def get_square(self):
        a = self.get_sides()[0]
        return 6 * a ** 2

    def get_volume(self):
        a = self.get_sides()[0]
        return a ** 3


# Код для проверки:
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
