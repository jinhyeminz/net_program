class MyCoplex:
    def __init__(self, real_1, imaginary_1, real_2, imaginary_2):
        self.real_1 = real_1
        self.imaginary_1 = imaginary_1
        self.real_2 = real_2
        self.imaginary_2 = imaginary_2
        
    def multi(self):
        result1 = self.real_1 * self.real_2 - self.imaginary_1 * self.imaginary_2
        result2 = self.real_1 * self.imaginary_2 + self.real_2 * self.imaginary_1

        """
        or

        a, b = self.real_1, self.imaginary_1
        c, d = self.real_2, self.imaginary_2

        result1 = a * c - b * d
        result2 = a * d + b * c

        if result2 >= 0:
            print(f'{result1}+{result2}')
        else:
            print(f'{result1}{result2}')

        """
    
        if result2 >= 0:
            print(f'{result1}+{result2}i')
        else:
            print(f'{result1}{result2}i')

mycomplex = MyCoplex(3, -4, -5, 2)
mycomplex.multi()