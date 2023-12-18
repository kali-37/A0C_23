def extrapolate(array):
    if all(x==0 for x in array):
        print("_______________________________________________")
        return 0 
    print(array)
    deltas=[y-x for x,y in zip(array,array[1:])] 
    diff =extrapolate(deltas) 
    print("DIFF",array[0]-diff)
    return array[0]-diff 

total =0 

for line in open('testcase.txt','r'):
    nums=list(map(int,line.split()))
    total+=extrapolate(nums)
print(total) 