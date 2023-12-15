from sys import argv 

# creating own class of _zip functionality to see how iter() works under the hood .
# we can directly use zip() in pyhton to zip the stuffs , by the way zip class is additional.
class _zip():
    def __init__(self,*args):
        self.iters=args 
        self.iter_count=len(args) 
        self.curr_index=0
    
    def __iter__(self):  
        return self.calculate_zip()
    
    def calculate_zip(self):
        _iters=[iter(its) for its in self.iters] 
        while(True):
            try:
                new_nexts=[next(it) for it in _iters ]
                yield tuple(new_nexts)
            except StopIteration:
                return

def __t_d_map(__given_time,__given_dist): # 

    mapper:dict[int,int]={}    
    for i in _zip(__given_time,__given_dist):
        max_dist=i[1]
        max_time=i[0]
        print(i)
        limit_gone=[]
        for j in range(max_time+1):
            limit_gone.append(j*(max_time-j))
        mapper[i]=len(list(filter(lambda x:x>max_dist,limit_gone)))
    
    mul=1
    for i in mapper.values():
        mul*=i 
    print("ans:" ,mul)
        


def main(dataset):
    __given_dist=0
    __given_time=int("".join(dataset[0].split()[1:]))
    __given_dist=int("".join(dataset[1].split()[1:]))
    print(__given_time,__given_dist)
    __t_d_map([__given_time],[__given_dist])
    ...


if __name__=="__main__":
    if len(argv)>=2:
        with open(argv[1],"r") as f :
            
            dataset=f.readlines()
            main(dataset)
    else:
        print("Usage: python3 part__.py <input.txt>")  