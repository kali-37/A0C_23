from sys import argv
calc_moves:dict[str,list[tuple]]={
    "|": [(-1,0),(1,0)],# UP , DOwn
    "-":[(0,-1) ,(0,1)], # left , right
    "L":[(1,0),(0,-1)],# Down , left
    "7":[(-1,0),(0,1)],# up , right
    "J":[(1,0),(0,1)], # down,right 
    "F":[(-1,0),(0,-1)], # up, left
    "S":[(-9,-9)],
    ".":[(-9,-9)],
    "\n":[(-9,-9)]
}
_directions=[[1,0],[-1,0],[0,-1],[0,1]]

class Node:
    _max_depth:int=0
    def __init__(self,value,x,y,_r_max,_c_max)->None:
        self.visited=False                  
        self.x=x                    
        self.y=y                    
        self.depth=0                    
        self.value=value       
        self.max=_r_max 
        self.min=_c_max 

    def start_search(self,matrix:list[list['Node']],_root:"Node"):
        queue:list[Node]=[_root] 
        while queue:
            _indx_node=queue.pop(0) 
            for  x,y in _directions:
                _dx,_dy=x+_indx_node.x ,y+_indx_node.y
                if ( 0<=_dx<=len(matrix)-1 \
                     and 0<=_dy<=len(matrix[self.x]) ):
                    if (x,y) in calc_moves[matrix[_dx][_dy].value] and matrix[_dx][_dy].visited==False :
                        _indx_node.visited=True 
                        _new_node=matrix[_dx][_dy]
                        _new_node.depth=_indx_node.depth+1 
                        if _indx_node.depth>self._max_depth:
                            self._max_depth=_indx_node.depth   
                        queue.append(_new_node)          
        return self._max_depth

def main(dataset):
    _root = None
    _max=len(dataset)
    matrix:list[list[Node]]=[]
    for r, i in enumerate(dataset):
        _list_Nodes :list[Node]= []
        for c, j in enumerate(i):
            _list_Nodes.append(Node(j, r, c,_max,len(i))) 
            if j == 'S':
                _root = _list_Nodes[-1]
        matrix.append(_list_Nodes)
    if _root:
        print(_root.start_search(matrix, _root)+1) # here  


if __name__=="__main__":
    if len(argv)>=2:
        with open(argv[1],"r") as f :
            dataset:list=f.readlines()
            main(dataset)
    else:
        print("Usage: python3 part__.py <input.txt>")  


        