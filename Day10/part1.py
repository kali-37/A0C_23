from sys import argv 

class Node:
    def __init__(self,value,x,y)->None:
        self.visited=False 
        self.x=x 
        self.y=y 
        self.depth=0 
        self.value=value

    def calc_moves(self):
        if self.value=='|':
            return [1,1,0,0]
        elif self.value=='-':
            return [0,0,1,1] 
        elif self.value=='L':
            return [1,0,1,0] # TOP BOTTOM RIGHT LEFT
        elif self.value=="7":
            return [0,1,0,1]
        elif self.value=="F":
            return [] 


def main(dataset):
    _list_Nodes=[]
    for r,i in enumerate(dataset):
        for c,j in enumerate(dataset):
            _list_Nodes.append(Node(j,r,c)) 
            if j=='S':
                _root=_list_Nodes[-1]








if __name__=="__main__":
    if len(argv)>=2:
        with open(argv[1],"r") as f :
            dataset:list=f.readlines()
            main(dataset)


    else:
        print("Usage: python3 part__.py <input.txt>")  