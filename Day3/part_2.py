from collections import defaultdict

def main():
    with open("input.txt","r") as f:
        dataset=f.readlines() 
    jk=len(dataset)
    gears:dict[tuple[int,int],list[int]]=defaultdict(list)
    for j in range(jk):
        n=0
        detected=False
        detecter=(0,0)
        for i in range(len(dataset[j])):
            if dataset[j][i].isdigit():
                n=n*10+int(dataset[j][i])
                for row in [-1,0,1]:
                    for col in [-1,0,1]:
                        if 0<=j+row<=jk-1 and 0<=i+col<=len(dataset[0])-1:
                            wilb=dataset[j+row][i+col]
                            if  not wilb.isdigit() and not wilb=='.\n' and wilb=="*":
                                detected=True
                                detecter=(j+row,col+i)
            elif   detected:
                gears[detecter].append(n)
                detected=False
                n=0

            else :
                n=0
    sum=0
    for i in gears.values():
        if len(i)==2: 
            sum+=i[0]*i[1]
    print(sum)


if __name__=="__main__":
    main()