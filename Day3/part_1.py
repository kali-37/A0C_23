def main():
    with open("input.txt","r") as f:
        dataset=f.readlines() 
    sume=0
    jk=len(dataset)
    satter=[]
    for j in range(jk):
        n=0
        detected=False
        for i in range(len(dataset[j])):
            if dataset[j][i].isdigit():
                n=n*10+int(dataset[j][i])
                for row in [-1,0,1]:
                    for col in [-1,0,1]:
                        if 0<=j+row<=jk-1 and 0<=i+col<=len(dataset[0])-1:
                            wilb=dataset[j+row][i+col]
                            if  not wilb.isdigit() and not wilb=='.' and wilb!="\n":
                                detected=True
            elif   detected:
                satter.append(n)
                sume+=n 
                detected=False
                n=0

            else :
                n=0
    print(sume,satter)
                    
            







        
if __name__=="__main__":
    main()




