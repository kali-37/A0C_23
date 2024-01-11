import {promises as fs} from 'fs';
const mapper={
    "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "0":0,
    "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "zero":0}
let _file_array=[] 

async function _handel(){
   const data=await fs.readFile("input_1.txt",{encoding:"utf-8"});
   _file_array=data.split('\n');
}


async function main(){
const dicter={}
let sum=0;
await _handel();
for (let i of  _file_array)    {
    dicter[i]=[]
    for (let key of Object.keys(mapper)){
    let temp=i.indexOf(key);
      while (temp!=-1){
            dicter[i].push([temp,mapper[key]])
            const temp_string=i.substring(temp+1,i.length);
            const newtemp=temp_string.indexOf(key);
            if (newtemp != -1) {
                temp +=newtemp+  1;}
          else{
            temp=newtemp;
          }
            // console.log(temp);
        }
    } 
}
        for (let val of Object.values(dicter)){
            val=val.sort((a,b)=>a[0]-b[0])
                sum+=val[0][1]*10+val[val.length-1][1];
            console.log(val);
        }
        console.log("SUM",sum);
}    


main();