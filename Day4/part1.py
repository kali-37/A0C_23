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
    length=0
    for i in frontline:
        lne=(len(frontline[i].intersection(set(i))))
        print(lne)
        if lne:
            length+=2**(lne-1)
    print(length)

if __name__=="__main__":
    if len(argv)>=2:
        with open(argv[1],"r") as f:
            dataset=f.readlines()
            main(dataset)
    else:
        print("Usage: python3 part__.py <input.txt>")
