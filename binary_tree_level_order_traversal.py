from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BFSSolution:
    def levelOrder(self, root) -> list[list[int]]:
        """
        TC: O(n)
        AS: O(n)
        """

        result = []
        queue = deque()

        # takes care of the root is None condition
        if root:
            queue.append(root)

        while queue:
            size = len(queue)
            same_level_nodes = []

            for _ in range(size): 
                node = queue.popleft()    
                same_level_nodes.append(node.val)         
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right) 
            
            result.append(same_level_nodes)

        return result

class DFSSolution:
    def levelOrder(self, root) -> list[list[int]]:

        # result variable will be 420 reference address
        # can be global or parameter of recursion 
        result = []
        
        def dfs(root, level, result):
            """
            TC: O(n)
            AS: O(h)
            """

            ## base condition
            if not root:
                return
            
            ## logic
            # if the length of result is equal to the level, meaning the that level list doesn't exits in memory
            # index of level start from 0
            if level == len(result): 
                result.append([])

            # add node to the level 
            result[level].append(root.val)
            # increment to next level
            level += 1

            # recursion
            dfs(root.left, level, result)
            dfs(root.right, level, result)


        dfs(root, 0, result)
        return result

if __name__ == "__main__":
    # root = [3,9,20,null,null,15,7]

    # Manually build the tree nodes and link them
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # ## BFS
    # bfs = BFSSolution()
    # print(bfs.levelOrder(root))

    # ## DFS
    dfs = DFSSolution()
    print(dfs.levelOrder(root))