x=10
y=10
def global_func():
    global x
    x+=10
    y=20
    print('x and y inside a function are',x,y)
global_func()    
print('x and y outside a function are',x,y)
