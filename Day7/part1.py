from sys import argv 
from collections import defaultdict

hand:dict[int,list]=defaultdict(list)

def rank_checker(_argv):
    _greatness="23456789TJQKA"
    for i in range(len(_greatness)):
        if _argv==_greatness[i]:
            return  i
    print("Remove Jocker card and re-sufttle")
    exit()

def indexer(_index ,_spl):
    _flag=False
    if hand[_index]:
        _counter=-1
        for i in  hand[_index]:
            _counter+=1
            for j in range(5):
                if rank_checker(i[j])<rank_checker(_spl[j]) :
                    break
                elif rank_checker(_spl[j])<rank_checker(i[j]):
                    hand[_index].insert(_counter,_spl)
                    _flag=True 
                    break 

            if _flag:
                break
    if not _flag:                 
        hand[_index].append(_spl)



def main(dataset):
    hash_rank:dict[str,int]={}
    counter:dict[str,int]={}
    for i in dataset:
        _spl1=i.split()  
        _spl=_spl1[0]     
        hash_rank[_spl]=int(_spl1[1])
        for k in _spl:
            counter[k]=(counter.get(k,0))+1
        _cou_var=counter.values()
        print(_spl,"   ",_cou_var)
        if 5 in _cou_var:  # five of kind
            indexer(6,_spl)
        elif 4 in _cou_var:  # four of kind
            # hand[5].append(_spl) 
            indexer(5,_spl)
        elif 3 in _cou_var and 2 in _cou_var: # house full
            indexer(4,_spl)
        elif  3 in _cou_var:  # Three of kind
            indexer(3,_spl)
        elif len((_cou_var))==3:  # Two pair
            indexer(2,_spl)
        elif 2 in _cou_var: # One pair
            indexer(1,_spl)
        elif len(_cou_var)==5: # High pair
            indexer(0,_spl)
        else:
            print("ERROR Occured",_cou_var) 
            exit()
        counter={} # reset counter 
            
    print(hand)

if __name__=="__main__":
    if len(argv)>=2:
        with open(argv[1],"r") as f :
            
            dataset=f.readlines()
            main(dataset)
    else:
        print("Usage: python3 part__.py <input.txt>")  