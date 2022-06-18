class Rectangle:
    "A class to manufacture rectangle objects"
    def __init__(self,xcor,ycor,w,h):
        """Initialize rectangle at posn, with width w, height h"""
        self.cornerx = xcor
        self.cornery = ycor
        self.width = w
        self.height = h
    def __str__(self):
        return"({0},{1},{2},{3})".format(self.cornerx, self.cornery, self.width, self.height)
    
box = Rectangle(0,0, 100, 200)
bomb = Rectangle(100,80, 5, 10)
print  ("box: ",box)
print ("bomb: ",bomb)

def create_rectangle(x,y,width,height):
   return Rectangle(x,y,width,height)
def str_rectangle(rect = Rectangle):
    return rect.__str__()
def shift_rectangle(rect,dx,dy):
    rect.cornerx = rect.cornerx + dx
    rect.cornery = rect.cornery + dy
def offset_rectangle(rect,dx,dy):
    new_rect = Rectangle(rect.cornerx+dx,rect.cornery+dy,rect.width,rect.height)
    return new_rect

r1 = create_rectangle(10, 20, 30, 40)
print(str_rectangle(r1))
shift_rectangle(r1, -10, -20)
print(str_rectangle(r1))
r2 = offset_rectangle(r1,100,100)
print(str_rectangle(r1))
print(str_rectangle(r2))
