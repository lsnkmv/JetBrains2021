class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1
        
class AVL_Tree:
    # Функция для осуществления логики добавления узла 
    # сбалансированного дерева, возвращает сбалансированное дерево
    def __init__(self):
        self.root_order = []

    def insert_to_AVL(self, root, key):
        
        # Проверка того, что добавленный узел больше или меньше
        # существующего узла в дереве, чтобы соответсвовать условию left < root < right
        if root is None:
            root = Node(key)
        elif key < root.data:
            root.left = self.insert_to_AVL(root.left, key)
        else:
            root.right = self.insert_to_AVL(root.right, key)
        
        # обновляем значение высоты узла дерева
        self._set_height(root) 
        
        # проверяем, сбалансировано ли дерево
        balance = self._check_balance(root)
        
        # если левая ветка "длиннее"
        
        # если добавляемое значение меньше значения левой ветки,
        # производим ротацию вправо
        if balance > 1 and key < root.left.data:
            return self._right_rotate(root)
        
        # если добавляемое значение больше значения левой ветки,
        # балансируем левую ветку, производим ротацию вправо
        if balance > 1 and key > root.left.data:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)
            
        # если правая ветка "длиннее"
    
        # если добавляемое значение больше значения правой ветки,
        # производим ротацию влево
        if balance < -1 and key > root.right.data:
            return self._left_rotate(root)
            
        # если добавляемое значение меньше значения правой ветки,
        # балансируем правую ветку, производим ротацию влево
        if balance < -1 and key < root.right.data:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)
        
        return root
    
 
    def _get_height(self, root):
        if not root:
            return 0
            
        return root.height
    
    def _set_height(self, root):
        if not root:
            return 0
        
        root.height = 1 + max(self._get_height(root.left),
                            self._get_height(root.right))
        
    def _check_balance(self, root):
        if not root:
            return 0
            
        return self._get_height(root.left) - self._get_height(root.right)
            
    def _left_rotate(self, root):
        
        Z = root.right
        temp = Z.left
        
        Z.left = root
        root.right = temp
        
        self._set_height(root)
        self._set_height(Z)
  
        return Z
    
    def _right_rotate(self, root):
        
        Z = root.left
        temp = Z.right
        
        Z.right = root
        root.left = temp
        
        self._set_height(root)
        self._set_height(Z)
  
        return Z
    
    def result_AVL_tree(self, root):
 
        if not root:
            return
 
        self.root_order.append(root.data)

        self.result_AVL_tree(root.left)
        self.result_AVL_tree(root.right)
