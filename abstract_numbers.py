from math import atan2, sin, cos, pi


class Number:
    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.mul(other)


class Complex(Number):
    def add(self, other):
        return ComplexRI(self.real + other.real, self.imag + other.imag)

    def mul(self, other):
        return ComplexMA(self.magnitude * other.magnitude, self.angle + other.angle)


class ComplexRI(Complex):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    @property
    def magnitude(self):
        return (self.real**2 + self.imag**2)**0.5

    @property
    def angle(self):
        return atan2(self.imag, self.real)

    def __repr__(self):
        return f"ComplexRI(real={self.real}, imag={self.imag})"


class ComplexMA(Complex):
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle

    @property
    def real(self):
        return self.magnitude * cos(self.angle)

    @property
    def imag(self):
        return self.magnitude * sin(self.angle)

    def __repr__(self):
        return f"ComplexMA(magnitude={self.magnitude}, angle={self.angle / pi} * pi)"
