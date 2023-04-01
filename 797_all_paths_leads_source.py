class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        output = []

        end = len(graph)-1

        def getPath(node,path,end):
            for i in node:
                temp_path = path[:]
                temp_path.append(i)
                if i == end:
                    output.append(temp_path)
                else:
                    getPath(graph[i],temp_path,end)

        getPath(graph[0],[0],end)

        return output

        
