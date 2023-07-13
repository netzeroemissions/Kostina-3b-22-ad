class GeometricFigure:
    def __init__(self, square, perimeter):
        self.square = square
        self.perimeter = perimeter

    def print_information(self):
        print(self.square, ' — Площадь, ', self.perimeter, ' — Периметр')