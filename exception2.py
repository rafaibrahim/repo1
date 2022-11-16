try:
   fh=open('testfile2.txt','r')
#    fh.write('hello')

except FileNotFoundError:
    print ('file doesnt exist')

else: 
    print('written')

finally:
    print('program executed')
    fh.close()
  
# fh=open('testfile.txt','r')
# fh.write('hello')
# fh.close()  