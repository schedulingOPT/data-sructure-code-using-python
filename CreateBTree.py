class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BTree:
    def CreateBTree(self,pres,i,ins,j,n):          #被CreateBTree1调用
        if n<=0: return None
        d=pres[i]                                   #取根结点值d
        root=TreeNode(d)							         #创建根结点(结点值为d)
        p=ins.index(d)                                  #在ins中找到根结点的索引
        k=p-j											#确定左子树中结点个数k
        root.left=self.CreateBTree(pres,i+1,ins,j,k)		    #递归构造左子树
        root.right=self.CreateBTree(pres,i+k+1,ins,p+1,n-k-1)	#递归构造右子树
        return root

    def DispBTree(self,root):		                #被DispBTree方法调用
        if root==None:                                 #空树返回空串
            return ""
        else:
            bstr=root.val							    #输出根结点值
            if root.left!=None or root.right!=None:
                bstr+="("							#有孩子结点时输出"("
                bstr+=self.DispBTree(root.left)	#递归输出左子树
                if root.right!=None:
                    bstr+=","						#有右孩子结点时输出","
                bstr+=self.DispBTree(root.right)	#递归输出右子树
                bstr+=")"							#输出")"
        return bstr