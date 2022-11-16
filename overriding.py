class Employee:
    def release_amount(self):
        return (5000)
class Manager:
    def release_amount(self):
        return(100000)

    @staticmethod    
    def add():
        print('hello world')    

object=Manager()
print(object.release_amount()) 
print(object.add())
