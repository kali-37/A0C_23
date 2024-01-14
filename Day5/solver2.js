const fs =require('fs') 

let dicter={}
let answer=[]
let _file_read=''

function calculate(seed){

    for (let i=1 ; i<=Object.keys(dicter).length;i++){
        for (let j=0;j<dicter[i].length;j++){
        if (seed>=dicter[i][j][1] && seed<=dicter[i][j][1]+dicter[i][j][2]){
           seed=seed - dicter[i][j][1]  +dicter[i][j][0]
            break;
        }
    }
}
answer.push(seed)
}
function main(){
    _file_read=fs.readFileSync(process.argv[2],"utf-8",'r').split('\n')
    let seeds=_file_read[0].match(/\d+/g).map(val=>parseInt(val));
    let seedrs=[]
    for (let i=0;i<seeds.length;i+=2){
        for (let j=seeds[i];j<=seeds[i+1]+seeds[i];j++){
            seedrs.push(j);
        }
    }
    console.log(seedrs)
    _file_read=_file_read.slice(1);
    let count=0;
    for (let index of _file_read){
        if (index.match('\\d+')){
            if (!dicter[count]){
               dicter[count]=[] 
            }
            dicter[count].push(index.match(/\d+/g).map(val=>parseInt(val)));
        }
        else if(index==''){
           count++; 
        }
     }
     
    for(let  x of  seeds){
    calculate(x)
    } 
    
    console.log(answer.sort((a,b)=>a-b)[0])

    }

main();