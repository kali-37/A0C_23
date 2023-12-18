from sys import argv 

def _recur(_prov:list[int])->int:
    if all([x==0 for x in _prov]):
         return 0 
    _new=[y-x for x,y in zip(_prov,_prov[1:])]
    _sum=_recur(_new)
    return _prov[0]-_sum
         
def main(dataset:list)->None:
        _sum=0
        for i in dataset:
            i=list(map(int,i.split()))
            _sum+=_recur(i)
        print(_sum)
if __name__=="__main__":
    if len(argv)>=2:
        with open(argv[1],"r") as f :
            dataset:list=f.readlines()
            main(dataset)


    else:
        print("Usage: python3 part__.py <input.txt>")  