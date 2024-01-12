const fs =require('fs') ;
let data=""
function readFile(){
    data =fs.readFileSync('input.txt','utf-8').split('\n');
}
let _sum=0
let _matrix=[];
for (let i of   [-1,0,1]){
    for (let j of  [-1,0,1]){
    _matrix.push([i,j]);
    }
}    
let star={}

let isdigit=_s=>/\d/.test(_s)
function main(){
    readFile();
    const _max_row=data.length;
    const _max_col=data[0].length;
    for (let row=0;row<_max_row;row++)
    {
        for (let col=0;col<_max_col;col++)
        {
            let detected_r=-19;
            let detected_c=-19;
            let _number=0
        if (isdigit(data[row][col]))
        {
           while(isdigit(data[row][col]))
           { 
           for (i of _matrix)
               {
                _r=i[0]+row;
                _c=i[1]+col;
                if (0<=_r && _r<_max_row && 0<=_c && _c<_max_col)
                {
                    console.log(detected_r,detected_c,">")

                    if (data[_r][_c]=="*"){
                    console.log("FOUND AG ",_r,_c);
                    detected_r=_r
                    detected_c=_c
                    break;
                }
                }
                }     
               
            
            _number=_number*10+parseInt(data[row][col]);
            if (col<_max_col) col++;
            if (col==_max_col) break;
        }

        // console.log("COMMIN Data",_number)
        if (detected_r!=-19){
        if (!star[[detected_r,detected_c]]){
            star[[detected_r,detected_c]]=[]
        }
        star[[detected_r,detected_c]].push(_number)
        }
    }
        }
    }
    for (let ind of Object.values(star)){
        let mul=1
        if (ind.length>1){
            for (let i=0;i<ind.length;i++){
                mul=mul*ind[i]
            }
        _sum+=mul;
        }
    }

    console.log(_sum)
}
main()