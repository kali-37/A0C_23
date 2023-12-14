from sys import argv
from collections import defaultdict
def main(dataset):
    seeds:list=list(map(int,dataset[0].split()[1:]))
    __dat:dict[int,list]=defaultdict(list)
    key=0
    for i in dataset[2:]:
        if i=="\n":
            key+=1
        
        if not ":"   in i and i !="\n":
            __dat[key].append(list(map(int,i.split())))
    __seed_lesser=[]
    __seed_val=0
    key=0
    __twoer=0
    __new_seed=[]
    n=0
    while(n<len(seeds)) :
        for i in range(seeds[n],seeds[n+1]+seeds[n]):
            # print(i,"I")
            __new_seed.append(i)
        n+=2

    seeds=__new_seed
    for i in seeds:
            __seed_val=i
            for key in __dat:
                for j in __dat[key]:
                    if j[1]<=__seed_val<=j[2]+j[1]-1:
                        # print(__seed_val,">>>>   " ,j[0],j[1],"><>>>>>><><       ",j[0]-j[1]+__seed_val)
                        __seed_val=j[0]-j[1]+__seed_val
                        break # if paile ko vayo vane , let's break , what's you waitin for....
                key+=1
            __seed_lesser.append(__seed_val)
    print(min(__seed_lesser))
    # print(seeds)


if __name__=="__main__":
    if len(argv)>=2:
        with open(argv[1],"r") as f :
            
            dataset=f.readlines()
            main(dataset)
    else:
        print("Usage: python3 part__.py <input.txt>")  