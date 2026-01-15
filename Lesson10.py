class Rectangle():
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def Rectangle_area(self):
        return self.width * self.length
        
newRectangle = Rectangle(12, 10) 
print('The dimensions of the rectangle - length: %d  width %d' % (newRectangle.width, newRectangle.length))
print("The area of the rectangle is:", newRectangle.Rectangle_area())