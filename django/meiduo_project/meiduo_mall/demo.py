class Node:
    """二叉树节点类"""

    def __init__(self, item):
        self.item = item  # 保持节点真实值
        self.lchild = None  # 左孩子指针
        self.rchild = None  # 右孩子指针


class BinaryTree:
    """二叉树"""

    def __init__(self, node=None):
        """给二叉树添加元素"""
        self.root = node

    def add(self, item):
        if self.root is None:
            self.root = Node(item)  # 是一颗空树的时候，直接将节点添加给根节点
        else:
            queue = [self.root]
            while len(queue) > 0:
                node = queue.pop(0)
                if not node.lchild:  # 如果左节点没有孩子，则添加元素并跳出循环
                    node.lchild = Node(item)
                    return
                else:
                    queue.append(node.lchild)
                if not node.rchild:  # 如果右节点没有孩子，则添加元素并跳出循环
                    node.rchild = Node(item)
                    return
                else:
                    queue.append(node.rchild)

    def breadth_travel(self):
        """
        广度优先遍历算法(横向)
        层次遍历
        """

        if self.root is None:
            return

        # 不是一颗空树
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.item, end=" ")
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)

    """
    深度优先遍历算法：
    先序遍历(根  左  右)
    中序遍历(左  根  右)
    后续遍历(左  右  根)
    """

    def preorder(self, root):
        """递归先序遍历"""
        if root == None:
            return
        print(root.item, end=" ")
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    def inorder(self, root):
        """递归中序遍历"""
        if root == None:
            return
        self.inorder(root.lchild)
        print(root.item, end=" ")
        self.inorder(root.rchild)

    def postorder(self, root):
        """递归后续遍历"""
        if root == None:
            return
        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.item, end=" ")


if __name__ == '__main__':
    tree = BinaryTree()
    [tree.add(i) for i in range(0, 10)]
    print(tree.breadth_travel())
    print(tree.preorder(tree.root))
    print(tree.inorder(tree.root))
    print(tree.postorder(tree.root))