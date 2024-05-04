class node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            new.next=self.head
            self.head.prev=new
            self.head=new
        self.tail.next=self.head
        
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            
            new=node(data)
            self.tail.next=new
            new.prev=self.tail
            self.tail=new
    def rev(self):
        curr=self.head
        
        while curr:
            if curr.next==None:
                self.head=curr
            curr.next,curr.prev=curr.prev,curr.next
            curr=curr.prev
            
               
    def delatbeg(self):
        self.head=self.head.next
        self.head.prev=None
    def delatend(self):
        self.tail=self.tail.prev
        self.tail.next=None     
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
l=[1,2,3,4,5]
o=dll()
for i in l:
    o.insertatend(i)
o.printing()
o.rev()
o.printing()
o.printing()