class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    
    def FindMin(self,root):        #設定一個查找最小值的function
        if root.left:
            return Solution().FindMin(root.left)
        else:
            return root
        
    def preorder(self,root,arr):    #設定一個可以遍歷的function
        if root == None:
            return arr
        else:
            arr.append(root.val) #如果root存在，把值append到array裡面
            if root.left != None:    #如果左節點存在，recursive
                Solution().preorder(root.left,arr)
            if root.right != None:  #如果右節點存在，recursive
                Solution().preorder(root.right,arr)
            return arr        
        
    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if root == None:
            root =TreeNode(val)
            return root
       # if val <= root.val:                          #考慮重複值的insert，把它insert到離root最近的地方
         #   SameNode = TreeNode(val)       #創建重複值的節點
           # SameNode.left = root.left          #重複值的左指針指向原本root的左節點
            #root.left = SameNode               #現在的root的左節點指向重複值節點
            #return   SameNode
        
        elif val<=root.val:
            if root.left:
                return Solution().insert(root.left, val)
            else:
                root.left = TreeNode(val)
                return root
        else:
            if root.right:
                return Solution().insert(root.right,val)
            else:
                root.right = TreeNode(val)
                return root        
         
 
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if target == root.val:            
            return root
        
        while root.right or root.left:                             #如果左節點不存在或者右節點不存在
            if target > root.val:
                return Solution().search(root.right,target)
            else:
                return Solution().search(root.left,target)
        return None
    
    
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        if Solution().search(root,target) != None:
            if target == root.val:                        #當刪去的節點是根節點時
                if root.right == None and root.left:                      #當根節點只有左節點時
                    root = root.left
                    return root
                elif root.left == None and root.right:                   #當根節點只有右節點時
                    root = root.right
                    return root
                elif root.right == None and root.left == None:     #當根節點沒有左右節點，即樹裡只有根節點
                    root = None
                    return root
                    
                else:                                                               #當根節點左右兩點都有時
                    minnode = self.FindMin(root.right)       
                    y = minnode.val
                    root = y
                    if minnode.right:
                            z = minnode.right
                            del minnode.right 
                            minnode = z
                    else:
                            del minnode
                            
            else:     #當刪去的節點不是根節點時，即target != root.val
                if target<=root.val:
                    self.delete(root.left,target)
                else:
                    self.delete(root.right,target)
                    
                return root
        else:
            return root
        
    def modify(self,root,target,new_val):
        if target != new_val:       
            self.insert(root,new_val)
            return Solution().delete(root,target)
        else:
            return root


#參考資料：https://blog.csdn.net/sinat_41029600/article/details/81878957
#https://blog.csdn.net/u011608357/article/details/35785553
