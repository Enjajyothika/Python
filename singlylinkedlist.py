'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=node(1)
a.next=node(2)
a.next.next=node(3)
print(a.data,a.next,a)
print(a.next.data,a.next.next,a.next)
print(a.next.next.data,a.next.next,a.next.next.next)'''
class node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            new.next=self.head
            self.head=new
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            i=self.head
            while i.next!=None:
                i=i.next
            i.next=new
    def insertatpos(self,data,pos):
        c=0
        i=self.head
        j=None
        if self.head==None and pos==1:
            self.head=node(data)
        
        elif i.next==None:
            if pos==1:
                new=node(data)
                new.next=i
                i=new
            elif pos==2:
                new=node(data)
                i.next=new
        else:
            new=node(data)
            j=None
            while(i.next!=None):
                c=c+1
                if pos==c:
                    break

                else:
                    j=i
                    i=i.next
            new.next=i
            j.next=new
            #new.next=i
    def rev(self):
        prev=None
        curr=self.head
        nxt=self.head.next
        while curr:
            if curr.next==None:
                self.head=curr
            curr.next=prev 
            prev=curr
            curr=nxt
            if nxt:
                nxt=nxt.next
            self.head=prev

    def delatbeg(self):
        i=self.head
        self.head=self.head.next
        i=None
        
            
        
    def delatend(self):
        if self.head==None:
            print("no list")
        else:
            i=self.head
            while(i.next!=None):
                p=i
                i=i.next
            p.next=None
            del i

    def printing(self):
        c=0
        if self.head==None:
            return
        i=self.head
        while(i):
            c=c+1
            print(i.data)
            i=i.next  
        print("lenght",c)    
l=[1,2,3,4,5,6]
d=7
pos=2
o=sll()
for i in l:
    o.insertatend(i)

#o.insertatpos(d,pos)
o.printing()
       
