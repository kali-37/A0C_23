let fs=require('fs');
const { exitCode } = require('process');

function main(){
    if (process.argv.length<3){
        console.log("Provide argv as inputfile.txt")
        process.exit()
     }
    const _file_read=fs.readFileSync(process.argv[2],"utf-8",'r').split('\n');
    console.log(_file_read) ;
    const _times=_file_read[0].match(/\d+/g).map(x=>parseInt(x));
    const _distances=_file_read[1].match(/\d+/g).map(x=>parseInt(x));
    console.log(_times)
    console.log(_distances)
    let _sumer=[]
     for (let i=0;i<_times.length;i++){
        // for (let _times[0]
         let _count=0;
            for (let j =0 ;j<_times[i];j++){
            if ((_times[i]-j)*j>_distances[i]){
                _count+=1;
            }
        }
        _sumer.push(_count)
     }
    console.log(_sumer)
    console.log("summer", _sumer.reduce((a, b) => a * b));
}

main();