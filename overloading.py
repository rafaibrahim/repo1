class Area:
    # def area(self,r):
    #     return(3.14*r*r)

    # def area(self,l,b):
        # return (l*b) 

    def area(self, l=0, r=0, b=0):
        if r!=0:
            return (3.14*r*r)
        else:
            return (l*b)    



object=Area()
print('area is', object.area(r=2))
print('area is', object.area(l=4,b=6))
print('area is', object.area(2,0,3))




class Student:
   def __init__(self, name, age ):
    self.name=name
    self.age=age
    
   def details(self):
    print('name is',self.name, ', age is', self.age)
 
   def __del__(self):
    print('object deleted')

object=Student('Rafa',23)
object.details()
del object
