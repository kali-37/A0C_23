import fs from 'fs';

let file_array = null;

async function reader() {
        await  fs.promises.readFile("input_1.txt", { encoding: "utf-8" })
        .then(data=>{
        file_array = data.split('\n');;
        })
    .catch(err=>{
        console.log(err);
    });
}
async function main(){
await reader();
var ans=[]
for(let line of file_array){
    let each="";
    for( let l of line){
        // console.log("PROVIDED \n",l);
        if (/\d/.test(l)){ // !NaN(char)  NaN: Not a Number 
            each+=l;
        } 
        
    }
    
    // console.log("EACH",each);
    ans.push(Number(each[0]+each%10));
}
    console.log(ans);
const sum=ans.reduce((a,b)=>a+b,0)
console.log(sum);


}

main()