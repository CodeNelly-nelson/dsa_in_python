class Cookie:
    def __init__(self, color):
        self.color = color
        
        
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
        
    
    
cookie_one = Cookie("green")
cookie_two = Cookie("blue")

print("***** Before Colors Was Changed*****")
print(f"Cookie one is {cookie_one.get_color()}")
print(f"Cookie two is {cookie_two.get_color()}")
print()

# Change colors
cookie_one.set_color("red")
cookie_two.set_color("pink")

print()
print("***** After Colors Was Changed*****")
print(f"Cookie one is {cookie_one.get_color()}")
print(f"Cookie two is {cookie_two.get_color()}")


x = "Nelson"
y = "Soh"
print("Before")
print("X: ",x)
print("Y: ",y)
print()

temp = x
x = y
y = temp
print("After")
print("X: ",x)
print("Y: ",y)


