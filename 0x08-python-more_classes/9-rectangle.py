#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """Rectangle Class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """get the Width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set  the Width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """__str__ method return rectangle in char '#'"""
        rectangle = ""
        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            if i == self.__height - 1:
                rectangle += (str(self.print_symbol) * self.__width)
            else:
                rectangle += (str(self.print_symbol) * self.__width) + "\n"
        return rectangle

    def __repr__(self):
        """ __repr__ method return Rectangle(width, height)"""
        rec_width = str(self.__width)
        rec_height = str(self.__height)

        rectangle = "Rectangle(" + rec_width + ", " + rec_height + ")"
        return rectangle

    def __del__(self):
        """print message"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Method return the bigger Rectangle"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance"""
        return cls(size, size)
