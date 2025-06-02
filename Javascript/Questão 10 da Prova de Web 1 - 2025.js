let x = 4;
let y = 7;

if(x < y){
    x ++;
    y --;
    if (x === y){
        console.log("Iguais");
    }
    else if (x > y){
        console.log("X é maior que Y");
    }
    else {
        console.log("Y é maior que X");
    }
}
else {
    console.log("X  não é menor que Y");
}