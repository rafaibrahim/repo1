#---------------LIST----------------
# list1=[1,'rafa',23]
# print(list1)
# list1[2]='robin'
# print(list1)
# list1.append('johnson')
# print(list1)
# list1.insert(2,'steve')
# print(list1)
# print(list1*3)
# list2=['table','chair',22,'bag',56]
# print(list1+list2)
# a=list1+list2
# print(a)
# list2.extend(list1)
# print(list2)
# list1.remove('johnson')
# print(list1)
# list2.pop(3)
# print(list2)
# del list2[5]
# print(list2)
# del list2
# print(list2)
# list2.clear()
# print(list2)



# -------------------TUPLES-----------------------------
# tuple1=('rafa','rahul','sanjay',12,23,34)
# print(tuple1[3])

#-------------------DICTIONARY--------------------------
# dict1={'name':'rafa','place':'mankav','mark':80,'name':'safa'}
# print(dict1)
# print(dict1['name'])
# print(dict1['mark'])
# dict1['mark']=56
# print(dict1['mark'])
# print(dict1)
# dict1['age']=23
# print(dict1)
# dict1['ph_no']=9895625415
# print(dict1)
# dict1.update({'address':'calicut-14'})
# print(dict1)
# dict1.pop('mark')
# print(dict1)
# dict1.popitem()
# print(dict1)
# del dict1['ph_no']
# print(dict1)
# dict1.clear()
# print(dict1)


#-------------------------SET----------------------
# set1={'lion','tiger','cat','dog','monkey','rabbit','lion'}
# print(set1)
# set1.add('donkey')
# print(set1)
# set2={'apple','mango','gauva','banana','kiwi','anaar'}
# set1.update(set2)
# print(set1)
# list3=['tomato','potato','onion']
# list3.extend(set1)

# print(list3)
# set1.update(list3)
# a=tuple(list3)
# print(a)


#----------------------------IF condition-------------------
# a=2
# b=5
# if a==4:
#  print(a)
# else: 
#  print(b)

# num1=int(input('enter a value')) 
# num2=int(input('enter a value')) 
# # num3=int(input(enter a value)) 

# if num1>num2:
#     print('num 1 is greater')

# elif num1==num2:
#     print('both are equal')

# else:
#     print("num 2 is greater")

# num1=int(input('enter a value')) 
# num2=int(input('enter a value')) 
# num3=int(input('enter a value')) 

# if num1>num2:
#     if num1>num3:
#         print('num1 is greater')
#     else:
#         print('num3 is greater')

# else:
#     if num2>num3:
#         print('num2 is greater')        
#     else:
#         print('num3 is greater') 

#-----------------------------FOR LOOP-------------------

# list1=['table','chair','shelf','bed','cupboard']
# for i in list1:
#     print(i)

# for i in range(3):
#     print(i)
 
# for x in range(1,6):
#     print(x) 

# for y in range(0,10,2):
#     print(y)

#---------------------BREAK-----------------

# a=input('enter a string')
# for i in a:
#     if i=='f':
#         break  
#     print(i)

#---------------------WHILE----------------  

# i=0
# while(i<5):
#     print(i)
#     i=i+1  


# password="rafa1234"
# guess=""
# count=0
# while True:
#     guess=input('enter a password')
#     if password==guess:
#         print('login success')
#         break
#     else:
#         print('login failed') 
#         count +=1
#         if count>2:
#             print('3 unsuccessful attempts'  )   
#             break

# a=input('enter a string')
# for i in a:
#     if i=='k':
#          continue
#     print(i)        

# a=input('enter a word')
# for i in a:
#     if( i in ['a','e','i','o','u']):
#         print (i)
#     else:
#          continue
#         pass
#         print('this never executed')
        

# numbers=[1,2,5,11,22,33,44,21,62]
# for i in numbers:
#     if i%5==0:
#         print(i)
#         break

# else:
#     print('not divisiblem by 5')     

#--------------------FUNCTIONS-----------------      
# def function1():
#     print('hello world')

# function1()    

# def sum(a,b):
#     print(a,b)
#     print ('sum=',a+b)
# a1=int(input('enter a number'))    
# a2=int(input('enter a number'))    
# sum(b=a1,a=a2)
 

# def add(a,b=10):
#     print(a,b)
#     print ('sum=',a+b)
# a1=int(input('enter a number'))    
# a2=int(input('enter a number'))    
# sum(b=a1,a=a2)
# add(20,30)

# def printdetails (*components,item):
#     print ('components of %s are' % (item))
#     for i in components:
#         print('-',i)
#     return
# printdetails ('computer','cpu','monitor',item='motherboard')

# def multiple(item,**things):
#     print(item)
#     for key,value in things.items():
#         print ('- %s is %s'%(key,value))
#     return 

# multiple ('computer',cpu=25,monitor=52,motherboard=14,speaker=54,mouse=45)

#----------------------FACTORIAL USING RECURSION-----------------

def fact(a):
    if a==1:
        return 1
    else:
        return a*fact(a-1) 
print ('factorial=',fact(5))        


    
