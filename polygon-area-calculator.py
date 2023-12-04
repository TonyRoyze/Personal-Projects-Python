class Rectangle:
  height = 0
  width = 0

  def __init__(self, width, height):
    self.height = height
    self.width = width

  def set_width(self, width):
    self.width = width
    
  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.height * self.width

  def get_perimeter(self):
    return self.height * 2 + self.width * 2

  def get_diagonal(self):
    return (self.height ** 2 + self.width ** 2) ** 0.5

  def get_picture(self):
    if self.height > 50 or self.width > 50:
      return "Too big for picture."
    else:
      picture = ""
      for i in range(self.height):
        picture += "*" * self.width + "\n"
      return picture

  def get_amount_inside(self, shape):
    return int(self.height / shape.height) * int(self.width / shape.width)

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
  
  def __init__(self, length):
    super().__init__(length, length)

  def set_side(self, length):
    self.height = length
    self.width = length

  def set_width(self, length):
    self.set_side(length)

  def __str__(self):
    return f"Square(side={self.height})"


      


  
