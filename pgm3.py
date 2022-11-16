x=10
y=10
def global_func():
    x=1
    y=2
    print('x and y inside a function are',x,y)
global_func()    
print('x and y outside a function are',x,y)
