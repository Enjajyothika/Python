n=int(input())
i=1
def a(n):
    for i in range(2,n):
        for j in range(2,i):
            if(i%j==0):
                break           
        else:
             print(i)       
a(n)
   

        
       

