class IntList:                              #整数表类
    m=2
    def __init__(self):			            #构造方法
        self.capacity=self.m			    #容量
        self.data=[0]*self.m				#动态数组
        self.length=0				        #长度
    def Expand(self):					    #按长度两倍扩大容量
        self.capacity=2*self.length			#设置新容量
        newdata=[0]*self.capacity
        for i in range(0,self.length):      #复制全部元素
            newdata[i]=self.data[i]
        self.data=newdata

    def Add(self,e):			#添加e
        if self.length==self.capacity:
            self.Expand()
        self.data[self.length]=e
        self.length+=1

    def  DispList(self):
        for i in range(0,self.length):
            print(self.data[i],end=' ')


L=IntList()
L.Add(1);
L.Add(2);
L.Add(3);
L.Add(4);
L.Add(5);
L.DispList()
