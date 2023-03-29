#  this utilizes lelvel order treversel

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        output = {}
        out = []
        def treverse(root,level): 
            if not root: return
            if level in output:
                output[level].append(root)
            else:
                output[level]=[root]
            treverse(root.left,level+1)
            treverse(root.right,level+1)
        

        treverse(root,0)
        for v in output.values():
            for i in range(len(v)):
                if i < len(v)-1:
                    v[i].next = v[i+1]
                else:
                    v[i].next = None


        return root

