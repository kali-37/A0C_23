
import re
# So, 12 red , 13 green and 14 blue have total of 39 

r=12
g=13
b=14

def main():
    sum=0
    with open("day_2.txt") as f:
        data=f.readlines()
        for i in data:
            a=re.match(r'Game (\d+)',i)
            if a:
                print(re.findall(r'(\d+) green',i))
                green=max(map(int,re.findall(r'(\d+) green',i)))
                red=max(map(int,re.findall(r'(\d+) red',i)))
                blue=max(map(int,re.findall(r'\b(\d+) blue',i)))
                # print("GREEN",red)
                # print("GGG",red,green,blue)
                if (green <= g and red <= r and blue <= b):
                    # print(a.group(1)) 
                    # print(a)
                    sum+=int(a.group(1))
                # print(type(green))
    print(sum) 

if __name__=='__main__' :
    main()