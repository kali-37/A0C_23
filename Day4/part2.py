from sys import argv
import re
# trying to use split method rather ,then regex and regex too..
def main(dataset):
    frontline: dict[tuple,set]={}
    TEMP1=""
    TEMP2=""
    pattern=r'\|\s*([\d\s]+)'
    for i in dataset:
        TEMP1=i[i.index(":")+1:i.index("|")-1].split()
        TEMP1=tuple(map(int,TEMP1))
        TEMP2=re.search(pattern,i)
        if TEMP2 :
            TEMP2=TEMP2.group(1).split()
            TEMP2=set(map(int,TEMP2)) 
            frontline[TEMP1]=TEMP2
    length=[]
    for i in frontline:
        lne=(len(frontline[i].intersection(set(i))))
        length.append(lne)
    instances=[1]*len(length) 
    n=0 
    while(n<=len(length)-1):
        print(n+1,n+1+length[n])
        for i in range(n+1,n+1+length[n]):
            instances[i]+=instances[n]
        n+=1 

    print(sum(instances)) 

if __name__=="__main__":
    if len(argv)>=2:
        with open(argv[1],"r") as f:
            dataset=f.readlines()
            main(dataset)
    else:
        print("Usage: python3 part__.py <input.txt>")