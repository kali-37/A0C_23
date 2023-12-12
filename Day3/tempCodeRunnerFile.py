 if dataset[j][i].isdigit():
                n=n*10+int(dataset[j][i])
                detected=False
                for row in [-1,0,1]:
                    for col in [-1,0,1]:
                        if 0<j+row<=len(dataset) and 0<i+col<=len(dataset[0]):
                            print(i,j)
                            wilb=dataset[j+row][i+col]
                            if  not (wilb.isdigit() and wilb=="."):
                                detected=True
                        
            elif n>0 and not (dataset[j][i].isdigit()) and detected:
                sum+=n 
                detected=False
                n=0
            elif n>0 and dataset[j][i].isdigit() and not  detected:
                continue 

        print(sum) 