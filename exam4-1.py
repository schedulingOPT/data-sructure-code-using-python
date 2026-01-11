from CreateBTree import TreeNode,BTree

def leafnodes(b):				#求二叉树b中的叶子结点个数
    if b==None:return 0														#空树
    if b.left==None and b.right==None:return 1						#只有一个叶子结点
    else:return leafnodes(b.left)+leafnodes(b.right) #其他情况

pres=['A','B','D','G','C','E','F']
ins=['D','G','B','A','E','C','F']
print("先序:",end=' '); print(pres)
print("中序:",end=' '); print(ins)
print("构造二叉树root")
bt=BTree()
root=bt.CreateBTree(pres,0,ins,0,len(pres))
bstr=bt.DispBTree(root)
print("叶子结点个数:",leafnodes(root))
