
let fs=require('fs');
let data_file=""
let sum=0;
function main(){
if (process.argv.length >=2){
    data_file=fs.readFileSync(process.argv[2], {flag: 'r',encoding:'utf-8'}).split('\n')
    for (let i of data_file){
        // _regx=new RegExp(".*:\\s+((\\d+\\s)*)\\|.*"); -> . split (' ')
        i=i.split('|') 
        _regx=new RegExp("\\b\\d+\\b","g")
        first_part =(i[0].split(':')[1].match(_regx).map(cel => parseInt(cel)));
        second_part= new Set(i[1].match(_regx).map(cel => parseInt(cel)));
        const intersections=[...first_part].filter(elm=>second_part.has(elm));

        if (intersections.length){
            console.log(intersections)
            sum+= 2**(intersections.length-1)
        }
    }
}
console.log(sum)
}
// ".*:\\s((\\d+\\s)*)\\|.*"
main();


