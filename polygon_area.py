class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def __str__(self):
        return "Rectangle(width={w}, height={h})".format(h=self.height, w=self.width)
    def set_width(self,widthparam): 
        self.width = widthparam
    def set_height(self,heightparam):
        self.height = heightparam
    def get_area(self):
        return (self.width*self.height)
    def get_perimeter(self):
        return (2 * (self.width + self.height))
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    def get_picture(self):
        a = ""
        pic = ''''''
        if self.width >= 50 or self.height >= 50:
            return "Too big for picture."
        else:
            for i in range(self.width):
                a += "*"
            for j in range(self.height):
                pic += a + "\n"
            return pic
    def get_amount_inside(self,square):
        vertical = self.height // square.height
        horizontal = self.width // square.width
        return (vertical * horizontal)


class Square(Rectangle):
    def __init__(self,side):
        self.width = side
        self.height = side
    def set_side(self,side):
        self.width = side
        self.height = side
    def __str__(self):
        return "Square(side={s})".format(s = self.width)