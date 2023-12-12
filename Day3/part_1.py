
def main():
    
    with open("input.txt","r") as f:
        dataset=f.readlines() 
    sume=0
    jk=len(dataset)
    satter=[]
    for j in range(jk):
        n=0
        detected=False
        for i in range(len(dataset[0])-1):
            print(n)
            print()
            # if i==len(dataset[0])-2:
            #     print("TRUE>>>",dataset[j][i])  
            # print(dataset[j][i]) 
            if dataset[j][i].isdigit():
                n=n*10+int(dataset[j][i])
                if i==8:
                    print("    " , i,j,"           ", dataset[j][i]  ) 
                for row in [-1,0,1]:
                    for col in [-1,0,1]:
                        if 0<=j+row<=jk-1 and 0<=i+col<=len(dataset[0])-1:
                            wilb=dataset[j+row][i+col]
                            if  not wilb.isdigit() and not wilb=='.':

                                detected=True
    
            elif  not dataset[j][i].isdigit() and detected:
                satter.append(n) 
                sume+=n 
                detected=False
                n=0
            elif  i==len(dataset[0])-2 and detected:
                satter.append(n) 
                sume+=n 
                detected=False 
            elif n>0 and not dataset[j][i].isdigit() and not detected :
                n=0
            

                

          


    print(sume,satter)
    print(sum(satter))

                    
            







        
if __name__=="__main__":
    main()

