const fs = require("fs");

let data_file=""
const r=12;
const b=14;
const g=13;
async function readfile(){
    try{
        data_file=(await fs.promises.readFile('day_2.txt',{encoding:"utf-8"})).split('\n');
    }
    catch(err){
        console.log(err);
    }
}

async function main(){
    let sum=0;
    let game_number="";
    await readfile();        
    for(let i of data_file)
    {
        dicter={}
        const regex0=new RegExp("Game\\s(\\d+):*");
        game_number=i.match(regex0)[1];
        const regex=new RegExp("\\d+ \\w+","g")
        let matchr=[...i.match(regex)]
            for (let j of  matchr){
            let [Num ,value]=j.split(' ')
            // console.log("NUM: ",Num);
            if (!dicter[value]){
            dicter[value]=-1
            }
            if (dicter[value]<+Num){
                dicter[value]=+Num;
            }
            }
            // console.log(dicter);

            if(dicter['red']<=r && dicter['blue']<=b && dicter['green']<=g){
                // console.log(game_number, "red :",dicter['red'] , dicter['blue'],dicter['green'], " green hai ");
                sum+=(+game_number);
            }   
 
    }
    console.log(sum)
    // console.log(data_file);
}
main()