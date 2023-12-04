def main():
    with open("input_1.txt") as f:
        data=f.readlines()
        word_to_num={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0}
        store:dict[str,list]={}
        for i in data:
            store[i]=[]
            for k in word_to_num.keys():
                x=i.find(k)
                while(x!=-1):
                    store[i].append((x,word_to_num[k]))
                    x=i.find(k,x+1)

        sum=0
        for i in store.values():
            i.sort()
            sum+=i[0][1]*10+i[-1][1]
        print(sum)

if __name__=='__main__':
    main()