class a:
    def fun(self):
        print("A")
class b(a):
    def __init__(self):
        print("constructor 1")
    def __init__(self):
        print("constructor 2")
    def fun(self):
        print("B")
class c:
    def fun1(self):
        print("C1")
    def fun1(self):
        print("c2")
class d(a,c):
    def fun2(self):
        print("d")
        
obj1=b()
obj1.fun()
o2=c()
o2.fun1()
o3=d()
o3.fun()
o3.fun1()
o3.fun2()