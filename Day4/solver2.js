let fs=require('fs');
let data_file=""
let sum=0;
let dicter={}

function main(){
if (process.argv.length >=2){
    data_file=fs.readFileSync(process.argv[2], {flag: 'r',encoding:'utf-8'}).split('\n')
    let count=1
    for (let i of data_file){
        // _regx=new RegExp(".*:\\s+((\\d+\\s)*)\\|.*"); -> . split (' ')
        i=i.split('|') 
        _regx=new RegExp("\\b\\d+\\b","g")
        first_part =(i[0].split(':')[1].match(_regx).map(cel => parseInt(cel)));
        second_part= new Set(i[1].match(_regx).map(cel => parseInt(cel)));
        const intersections=[...first_part].filter(elm=>second_part.has(elm));

        for (let i =count ;i<=count+intersections.length;i++){
            if (!dicter[i]){
                dicter[i]=0
            }  
            if (i==count) dicter[i]+=1 
            else dicter[i]+=dicter[count]
        }
        count++; 
    }
}
console.log(dicter)
let _sum=0
for (let val of Object.values(dicter)){
    _sum+=val; 
}
console.log("SUM IS ",_sum);
}
// ".*:\\s((\\d+\\s)*)\\|.*"
main();
