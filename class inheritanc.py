class a:
    def fun1(self):
        print("fun1")
class b(a):
    def fun2(self):
        print("fun2")
        
obj1=b()
obj1.fun1()

'''class a:
    def fun1(self):
        print("fun1")
class b:
    def fun2(self):
        print("fun2")
class c(a,b):
    def fun3(self):
        print("fun3")       
obj1=b()
obj1.fun1()
'''