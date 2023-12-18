from sys import argv 

def _recur(_prov:list[int],_sum:int)->int:
    _new=[]
    if ([_prov[0]]*len(_prov)!=_prov):
        for i in range(len(_prov)-1):
            _new.append(_prov[i+1]-_prov[i])
        _sum+=_new[-1]
        return _recur(_new,_sum)
    else:
        return _sum


def main(dataset:list)->None:
        dataset = [list(map(int,i.rstrip("\n").split())) for i in dataset]
        _sum:int=0 
        for i in dataset:
            _sum+=_recur(i,i[-1])          
        print(_sum)
if __name__=="__main__":
    if len(argv)>=2:
        with open(argv[1],"r") as f :
            dataset:list=f.readlines()
            main(dataset)


    else:
        print("Usage: python3 part__.py <input.txt>")  