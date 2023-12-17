from sys import argv 
import re


def main(dataset:list)->None:
    _mover:str=dataset[0].split("\n")[0]
    _mapper:dict[str,tuple]={}
    for i in dataset[2:]:
        _prompt=re.match(r"([A-Z]+)\s=\s\(([A-Z]+),\s([A-Z]+)\)|\n",i)
        if _prompt:
            _mapper[_prompt.group(1)]=(_prompt.group(2,3))
    _curr_key="AAA"
    Flag=True
    _c=0
    while Flag:
        _ind=_mover[_c % len(_mover)]
        if _curr_key=="ZZZ":
            Flag=False
        if _ind=="L":
            _curr_key=_mapper[_curr_key][0]
        elif _ind=="R":
            _curr_key=_mapper[_curr_key][1]
        _c+=1
        
    print(_c-1)
    



if __name__=="__main__":
    if len(argv)>=2:
        with open(argv[1],"r") as f :
            dataset:list=f.readlines()
            main(dataset)
    else:
        print("Usage: python3 part__.py <input.txt>")  