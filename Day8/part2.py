from sys import argv 
import re
import math

def main(dataset:list)->None:
    _mover:str=dataset[0].split("\n")[0]
    _mapper:dict[str,tuple]={}
    _With_A=[]
    for i in dataset[2:]:
        parent,child1,child2=re.search(r"(...)\s=\s\((...),\s(...)\)|\n",i).groups(0)
        if parent:
            _mapper[parent]=(child1,child2)
            if "A" in  parent:
                _With_A.append(parent)

    def _counts(_curr_key):
        Flag=True
        _c=0
        while not "Z" in _curr_key:
            _ind=_mover[_c % len(_mover)]
            if _ind=="L":
                _curr_key=_mapper[_curr_key][0]
            elif _ind=="R":
                _curr_key=_mapper[_curr_key][1]
            _c+=1
        return _c

    _cycles=[_counts(k) for k in _With_A]
    _lcm=_cycles[0]
    for num in _cycles[1:]:
        _lcm=math.lcm(_lcm,num)
    print(_lcm)
if __name__=="__main__":
    if len(argv)>=2:
        with open(argv[1],"r") as f :
            dataset:list=f.readlines()
            main(dataset)
    else:
        print("Usage: python3 part__.py <input.txt>")  