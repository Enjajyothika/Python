'''try:
    l=[1,2]
    print(l[1])
except:
    print("jyothika")
finally:
    print("finally")'''

def fun(l,ind):
    try:
        a=l.copy()
        a[0]=l[0]/l[ind]
    except ValueError:
        print("value error")
l=[1,2,3,4,5]
try:
    fun(l,5)
except IndexError:
    print("index error")
finally:
    print("end of block")
#raise ValueError("najdhbfhbfh")
