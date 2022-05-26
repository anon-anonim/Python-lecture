class Color:
    red = 0
    green = 0
    blue = 0

    def __init__(self, r,g,b):
         self.red = r
         self.green = g
         self.blue = b

    def toHex (self):
        return '#%02x%02x%02x' % (self.red, self.green, self.blue)

# gray = Color()
# gray.red = 80
# gray.green = 80
# gray.blue = 80

gray = Color (80,80,80)

b = gray.toHex()
print(b)
