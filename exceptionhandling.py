
# num1=int(input('enter first number'))
# num2=int(input('enter second number'))
# div=num1/num2
# print (div)
try:
    num1=int(input('enter first number'))
    num2=int(input('enter second number'))
    div=num1/num2
    print (div)
# except Exception as e:
#     print (e)
#     print('you cannot divide number with zero')  

except ValueError:
    print('invalid format')
except ZeroDivisionError:
    print('cannot divide by zero')
except FileNotFoundError:
    print('file doesnt exist')   

else:
    print('no exception')         

finally:
    print('program always works')




        
  