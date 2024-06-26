class Rectangle:
    def set_dimensions(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        return (self.l*self.b)
    
    def perimeter(self):
        return 2*(self.l+self.b)
         

r1=Rectangle()
r1.set_dimensions(4,3)
print("Length and breadth are:",r1.l,r1.b)
print("Area is :",r1.area())
print("Perimetre is :",r1.perimeter())