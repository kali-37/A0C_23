
from re import A


def main():
    sum=0
    pattern=set()
    with open("input.txt") as f:
        dataset=f.readlines()
    for i in dataset :
        k=0
        for j in i:
            if j !="." and not j.isdigit():
                pattern.add(k) 
            k+=1
    for i in dataset:
        k=0
        lister={}   
        for j in i:
            lister[k]=j
            if j.isdigit() :
                if k in pattern:
                    l=k-1
                    par=""
                    while(i[l].isdigit()):
                        par=i[l]+par
                        l-=1
                    while(i[k].isdigit()):
                        par+=i[k]
                        k+=1
                    j=i[k]
                    print(par)
            k+=1 
        # print(lister.values())



if __name__=="__main__":
    main()