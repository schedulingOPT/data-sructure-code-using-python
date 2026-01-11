from CreateBTree import TreeNode,BTree

def same(r1,r2):		#递归算法：判断r1和r2是否相同
	if r1==None and r2==None:
		return True
	elif r1==None or r2==None:
		return False
	if r1.val!=r2.val:
		return False
	leftans=same(r1.left,r2.left)					#递归调用1
	rightans=same(r1.right,r2.right)				#递归调用2
	return leftans and rightans

pres1=['A','B','D','G','C','E','F']
ins1=['D','G','B','A','E','C','F']
print("先序1:",end=' '); print(pres1)
print("中序1:",end=' '); print(ins1)
print("构造二叉树root1")
bt=BTree()
root1=bt.CreateBTree(pres1,0,ins1,0,len(pres1))
bstr1=bt.DispBTree(root1)
print("root1:",bstr1,end=' ')
print()

pres2=['A','B','C','D']
ins2=['B','A','D','C']
print("先序2:",end=' '); print(pres2)
print("中序2:",end=' '); print(ins2)
print("构造二叉树root2")
root2=bt.CreateBTree(pres2,0,ins2,0,len(pres2))
bstr2=bt.DispBTree(root2)
print("root2:",bstr2,end=' ')
print()
print("ans:",same(root1,root2))