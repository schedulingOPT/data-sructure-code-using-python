class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        ans=True;               #ans表示是否为完全二叉树
        bj=True;                #bj表示是否所有结点均有左右孩子
        qu=deque()              #定义一个队列
        qu.append(root)                                             #根结点进队
        while qu:
            p=qu.popleft()                                  #出队一个结点p
            if p.left==None:                                        #结点p没有左孩子
                bj=False
                if p.right!=None:ans=False                  #没有左孩子但有右孩子, 违反(1)
            else:                               #结点p有左孩子
                if bj==True:                            #所有结点均有左右孩子
                    qu.append(p.left)                       #左孩子进队
                    if p.right==None:bj=False   #结点p有左孩子但无右孩子,则bj置为假
                    else:qu.append(p.right)     #结点p有右孩子,将其进队
                else:ans=False                  #bj为假则ans为假, 违反(2)
        return ans